from .models import Post
from django.forms import ModelForm

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('author','date_posted')

        def __init__(self, *args, **kwargs):
            self.author = kwargs.pop('user')
            super(PostCreateForm, self).__init__(*args,**kwargs)