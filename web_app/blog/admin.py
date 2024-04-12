from django.contrib import admin

from .models import PostTopic, Post, PostComment

admin.site.register(PostTopic)
admin.site.register(Post)
admin.site.register(PostComment) # testing