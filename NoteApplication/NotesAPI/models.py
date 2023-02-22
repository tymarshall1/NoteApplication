from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    note = models.TextField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user.username) + "'s Note"
