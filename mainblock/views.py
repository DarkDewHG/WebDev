from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-date_posted']
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post




