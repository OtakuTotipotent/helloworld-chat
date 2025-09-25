from django.db import models
from django.contrib.auth.models import User as AuthUser


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=200, null=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    contact = models.ManyToManyField(AuthUser, related_name="contacts")

    def __str__(self):
        return f"{self.user.username}"
