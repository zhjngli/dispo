from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create/', views.create_user),
    path('posts/create/', views.create_post),
    path('posts/like/', views.like_post),
    path('users/top/', views.get_top_users),
    path('users/follow/', views.follow),
    path('users/feed/<int:user_id>/', views.get_user_feed),
]
