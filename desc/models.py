from django.db import models


class Task(models.Model):
    # creator = models.ForeignKey()
    theme = models.CharField(max_length=200)
    text = models.TextField()