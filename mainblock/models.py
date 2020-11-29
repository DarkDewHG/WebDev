from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post (models.Model):
    title = models.CharField(max_length=120) # заголовок поста
    date_posted = models.DateTimeField(default=timezone.now) # дата публикации
    content = models.TextField(max_length=10000) # текст поста
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

