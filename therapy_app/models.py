from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, *args, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.type = kwargs.get('type', 'Client')
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, *args, **kwargs):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.type = kwargs.get('type', 'Client')
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.type = kwargs.get('type', 'Client')
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    type = models.CharField(max_length=255, choices=(
        ('Client', 'Client'),
        ('Therapist', 'Therapist'),
    ))
    journal = models.CharField(max_length=255, null=True, blank=True)   # Only for Clients

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type']    # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active


class Mapping(models.Model):
    """
    This model will represent the relations between client and therapist
    if a client has mapped a therapist then this model will show an entry.
    along with the journal access.
    """
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mapping_client',
                               limit_choices_to={"type": "Client"})
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mapping_therapist',
                                  limit_choices_to={"type": "Therapist"})
    journal_access = models.BooleanField(default=False)
    journal_requested = models.CharField(max_length=255, choices=(
        ("Approved", "Approved"),
        ("Declined", "Declined"),
        ("Pending", "Pending"),
        ("Not Requested", "Not Requested"),
    ), default='Not Requested')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class Chat(models.Model):
    """
    This Model will store all the messages that are exchanged between a client and a therapist.
    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_from')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_to')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # will use this field to show the time of the message
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class Emotion(models.Model):
    """
    This model will store the emotions felt by the client.
    """
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emotion_client',
                               limit_choices_to={"type": "Client"})
    emotion = models.CharField(max_length=255, choices=(
        ("Happiness", "Happiness"),
        ("Caring", "Caring"),
        ("Depression", "Depression"),
        ("Inadequate", "Inadequate"),
        ("Fear", "Fear"),
        ("Confusion", "Confusion"),
        ("Hurt", "Hurt"),
        ("Anger", "Anger"),
        ("Loneliness", "Loneliness"),
        ("Remorse", "Remorse"),
    ))
    intensity = models.CharField(max_length=255, choices=(
        ("Strong", "Strong"),
        ("Medium", "Medium"),
        ("Light", "Light"),
    ))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # will use this field to show the time of the message
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class MappingRequest(models.Model):
    """
    Whenever a client or a therapist request someone to be mapped,
    that data will be stored in this model.
    """
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_whom')
    status = models.CharField(max_length=255, choices=(
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ), default="Pending")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    # whenever a request is approved or declined is_deleted should turn to True.


class Session(models.Model):
    """
    Details of each session will be stored here including requested sessions by clients.
    """
    mapping = models.ForeignKey(Mapping, on_delete=models.CASCADE, related_name='session_mapping')
    private_note = models.CharField(max_length=255, null=True, blank=True)
    shared_note = models.CharField(max_length=255, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=255, choices=(
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ('Declined', 'Declined'),
    ), default="Pending")
    # When a therapist creates a session, status should be approved.
    # When a client requests a session, status should be pending.
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
