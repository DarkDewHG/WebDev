from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    is_approved = models.BooleanField(default=False)
    rank_name = models.CharField(max_length=50, default='')
    bio = models.TextField(max_length=400,default='')

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_porfile_owner(self):
        return self.user

    def get_profile_name(self):
        if self.rank_name != '':
            return f'{self.nickname} [{self.rank_name}]'
        else:
            return f'{self.nickname}'

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('profile',args=[str(self.user.id)])

class CommentProfile (models.Model):
    content = models.TextField(max_length=600)
    profile = models.ForeignKey (Profile, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey (User,on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    """def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.post.id)])"""