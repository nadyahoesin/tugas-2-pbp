from django.db import models
from django.conf import settings

class Task(models.Model):
    # https://stackoverflow.com/questions/34305805/foreignkey-user-in-models
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()