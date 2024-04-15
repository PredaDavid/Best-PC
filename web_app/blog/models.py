from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostTopic(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(PostTopic, on_delete=models.SET_NULL, null=True, related_name="posts")
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return self.title
    
class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.content[:50]