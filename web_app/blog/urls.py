from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    
    path("", views.home, name="home"),
    path("post/<str:pk>/", views.post, name="post"),
    
    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-post'),
    path('delete-comment/<str:pk>/', views.deleteComment, name='delete-comment')
]