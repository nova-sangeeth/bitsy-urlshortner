from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class short_urls(models.Model):
    short_url = models.CharField(max_length=20, null=True)
    long_url = models.URLField("URL", max_length=512)
    slug = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.short_url


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    age = models.IntegerField(null=True)
    occupation_sector = models.CharField(null=True, max_length=64)
    country = models.CharField(null=True, max_length=24)

    def __str__(self):
        return str(self.user)

