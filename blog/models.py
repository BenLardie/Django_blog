from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateField()
    author = models.CharField(max_length=255)

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    Article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
