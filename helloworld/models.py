from django.db import models
from django.contrib.auth.models import User as AuthUser


class Contact(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    contact = models.ManyToManyField(AuthUser, related_name="contacts")

    def __str__(self):
        return f"{self.user.username}"
