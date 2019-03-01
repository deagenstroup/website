from django.db import models


class ProjectPage(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=1024)
    shortdesc = models.CharField(max_length=2048)
    body = models.TextField()

