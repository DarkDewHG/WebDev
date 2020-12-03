from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import HttpResponseRedirect
from .models import Post,Comment
from .forms import CommentCreateForm


class PostListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = reverse_lazy('login')
    model = Post
    template_name = "mainblock/home.html"
    ordering = ['-is_pinned','-date_posted']


def post_detail_view(request,pk):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = request.user
            com.post = Post.objects.get(id = pk)
            com.save()
        return redirect(post.get_absolute_url())
    else:
        form = CommentCreateForm()
        object = Post.objects.get(id = pk)
        return render(request,'mainblock/post-detail.html',{'form': form, 'object': object})



class PostCreateView(CreateView):
    model = Post
    template_name = 'mainblock/create-post.html'
    fields = ['title','content']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'mainblock/edit-post.html'
    fields = ['title','content','date_posted','author']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'mainblock/delete-post.html'
    success_url = reverse_lazy('home')



