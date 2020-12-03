from django.shortcuts import render,HttpResponse

from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import CommentProfileCreateForm,ProfileUpdateForm
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
        return redirect(profile.get_absolute_url())
    else:
        form = CommentProfileCreateForm()
        object = User.objects.get(id=pk).profile
        return render(request,'registration/profile.html',{'form': form, 'object': object})


def profile_update_view(request,pk):
    prof = Profile.objects.get(id= pk)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=Profile.objects.get(id= pk))
        print (p_form)
        if p_form.is_valid():
            p_form.save()
            return redirect(prof.get_absolute_url())
    else:
        p_form = ProfileUpdateForm(instance=Profile.objects.get(id= pk))
    context = {'form' : p_form,'object' : prof}


    return render(request,'registration/profile_update.html',context)

