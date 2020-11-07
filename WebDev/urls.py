from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from usersblock import views as user_views
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainblock.urls')),

    ##Userblock urls##
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Userblock/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Userblock/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
