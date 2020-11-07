from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #ProfilePic = models.ImageField(default='defaultProfilePic.jpg', upload_to='profile_pics')
    #McSkin = models.ImageField(default='defaultMcSkin.jpg', upload_to='McSkins')
    #UserVerification = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
