from .models import CommentProfile,Profile
from django import forms


class CommentProfileCreateForm(forms.ModelForm):
    class Meta:
        model = CommentProfile
        fields = ('content',)

        def __init__(self, *args, **kwargs):
            self.author = kwargs.pop('user')
            self.post = kwargs.pop('post')
            super(CommentProfileCreateForm, self).__init__(*args,**kwargs)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image','nickname','bio' ,'rank_name','is_approved')