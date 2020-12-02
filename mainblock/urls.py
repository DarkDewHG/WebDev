from django.urls import path
from .views import (PostListView,
                    post_detail_view,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    )


urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]