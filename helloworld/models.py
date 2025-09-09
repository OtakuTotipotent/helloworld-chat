from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=200, null=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
