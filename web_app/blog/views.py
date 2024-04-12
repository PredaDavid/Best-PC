from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from .models import Post, PostTopic, PostComment
from .forms import PostForm


def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username dose not exist')
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password is incorrect')
        
    
    context = {
        'page': page,
    }
    return render(request, "blog/login_register.html", context)

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    context = {
        'page': page,
        'form': form,
    }
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'An error has occurred during registration')    
    
    return render(request, "blog/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q')
    if q:
        posts = Post.objects.filter(
            Q(topic__name__icontains=q) | Q(title__icontains=q) 
            )
    else:
        posts = Post.objects.all()
    
    
    post_topics = PostTopic.objects.all()
    context = {
        "post_topics": post_topics,
        "posts": posts,
        "posts_count": posts.count()
    }
    return render(request, "blog/home.html", context)

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.postcomment_set.all().order_by('-created')
    likes = post.likes.all()
    had_liked = post.likes.filter(id=request.user.id).exists()
    
    
    if request.method == 'POST':
        if 'like' in request.POST:
            post.likes.add(request.user)
            return redirect('post', pk=post.pk)
        elif 'dislike' in request.POST:
            post.likes.remove(request.user)
            return redirect('post', pk=post.pk)
        elif 'comment':
            content = request.POST.get('content')
            if content:
                comment = PostComment.objects.create(
                    user=request.user,
                    post=post,
                    content=content
                )
                comment.save()
                return redirect('post', pk=post.pk)
    
    
    context = {
        "post": post,
        "comments": comments,
        "likes": likes,
        'had_liked': had_liked,
    }
    
    return render(request, "blog/post.html", context)

@login_required(login_url='login')
def createPost(request):
    if request.user.is_superuser is False:
        return HttpResponse('You are not allowed to create a post')
    
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, "blog/post_form.html", context)

def updatePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    
    if request.user.is_superuser is False:
        return HttpResponse('You are not allowed to update a post')
    
    if request.user != post.author:
        return HttpResponse('You are not allowed to edit this post')
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, "blog/post_form.html", context)

def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user.is_superuser is False:
        return HttpResponse('You are not allowed to delete a post')
    
    if request.user != post.author:
        return HttpResponse('You are not allowed to delete this post')
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context = {'post': post, 'obj': post}
    return render(request, "blog/delete.html", context)

def deleteComment(request, pk):
    comment = get_object_or_404(PostComment, pk=pk)
    
    if request.user != comment.user:
        return HttpResponse('You are not allowed to delete this post')
    
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    
    context = {'obj': comment}
    return render(request, "blog/delete.html", context)