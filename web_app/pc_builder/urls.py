from django.urls import path
from . import views

urlpatterns = [
    path("configure-pc", views.configure_pc, name="configure-pc"),
    path("choose-part/<str:type>/", views.choose_part, name="choose-part"),
    
    path("add-part/<str:type>/<int:id>/", views.add_part, name="add-part"),
    path("remove-part/<str:type>/", views.remove_part, name="remove-part"),
]