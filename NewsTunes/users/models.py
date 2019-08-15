# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import utc


class CustomUser(AbstractUser):
    business = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)
    opinion = models.BooleanField(default=False)
    world = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    health = models.BooleanField(default=False)
    usa = models.BooleanField(default=False)
    style = models.BooleanField(default=False)
    travel = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class News(models.Model):
    headline = models.CharField(max_length=1000)
    body = models.TextField()
    date = models.TextField()
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    posttime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.headline

    def get_time_diff(self):
        if self.posttime:
            now = datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.posttime
            return timediff.total_seconds()
