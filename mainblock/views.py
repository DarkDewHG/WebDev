from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import HttpResponseRedirect
from .models import Post


class PostListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = reverse_lazy('login')
    model = Post
    template_name = "mainblock/home.html"
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = "mainblock/post-detail.html"
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'mainblock/create-post.html'
    fields = ['title','content']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())





