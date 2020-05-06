from django.db import models

# Blog model created below


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.DateField()
