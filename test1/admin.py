from django.contrib import admin

from .models import Post
from test2.models import Comment

admin.site.register(Post)
admin.site.register(Comment)
