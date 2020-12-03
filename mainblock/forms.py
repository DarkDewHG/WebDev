from .models import Post, Comment
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author','date_posted')

        def __init__(self, *args, **kwargs):
            self.author = kwargs.pop('user')
            super(PostCreateForm, self).__init__(*args,**kwargs)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        def __init__(self, *args, **kwargs):
            self.author = kwargs.pop('user')
            self.post = kwargs.pop('post')
            super(CommentCreateForm, self).__init__(*args,**kwargs)


