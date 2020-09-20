from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

    def __str__(self):
        return f"Username: {self.username} email: {self.email}"

class Listing(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    startingbid = models.IntegerField()
    imageurl = models.CharField(blank=True, max_length=256)
    category = models.CharField(blank=True, max_length=128)
    created = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    bidcount = models.IntegerField(default=0)
    price = models.IntegerField()
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="wins", null=True)

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ManyToManyField(Listing, blank=True, related_name="comments")    

class Bids(models.Model):
    bid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ManyToManyField(Listing, blank=True, related_name="bids")

class Wishlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True, related_name="wishlist")
