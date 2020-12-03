from django.urls import path
from .views import RegisterView,profile_view,profile_update_view


urlpatterns = [
    path('signup/',RegisterView.as_view(),name='signup_page'),
    path('profile/<int:pk>',profile_view,name='profile'),
    path('profile/edit/<int:pk>',profile_update_view,name='profile_update')


]