from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post (models.Model):
    title = models.CharField(max_length=120) # заголовок поста
    date_posted = models.DateTimeField(default=timezone.now) # дата публикации
    content = models.TextField(max_length=10000) # текст поста
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False)
    for_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])


class Comment (models.Model):
    content = models.TextField(max_length=100)
    post = models.ForeignKey (Post, on_delete=models.CASCADE)
    author = models.ForeignKey (User,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.post.id)])


