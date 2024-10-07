from django.urls import path
from . import views as api_views

urlpatterns = [
    path('todos/', api_views.todo_list_create, name = 'todo_list'),
    path('todos/<int:pk>', api_views.todo_list_detail, name = 'todo_detail'),
]