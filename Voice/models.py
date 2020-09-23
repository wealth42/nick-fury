from django.db import models

# Create your models here.
class Signature(models.Model):
    sign_upload = models.ImageField(upload_to='images/') 