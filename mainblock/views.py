from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts = [
    {
        'author': 'Me',
        'title': 'First Title of the post   ',
        'content': 'First post',
        'date_posted': 'Today',
    },
    {
        'author': 'You',
        'title': 'Second Title of the post   ',
        'content': 'Second post',
        'date_posted': 'Tomorrow',
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post.html', context)


def about(request):
    return HttpResponse('<h1> Hello there1</h1>')
# Create your views here.
