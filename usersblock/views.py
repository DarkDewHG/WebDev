from django.shortcuts import render,HttpResponse

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import CommentProfileCreateForm
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import redirect


class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def profile_view(request,pk):
    if request.method == 'POST':
        form = CommentProfileCreateForm(request.POST)
        profile = User.objects.get(id=pk).profile
        if form.is_valid():
            com = form.save(commit=False)
            com.author = request.user
            com.profile = profile
            com.save()
        print(profile)
        return redirect(profile.get_absolute_url())
    else:
        form = CommentProfileCreateForm()
        object = User.objects.get(id=pk).profile
        return render(request,'registration/profile.html',{'form': form, 'object': object})