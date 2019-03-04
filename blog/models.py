from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = datetime.DateField.auto_now
    author = models.CharField()
