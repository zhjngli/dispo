from django.contrib import admin
from .models import Post, PostLike, UserFollow

# Register your models here.
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(UserFollow)
