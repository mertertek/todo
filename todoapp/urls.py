from django.urls import path
from . import views as api_views

urlpatterns = [
    path('', api_views.TodoListCreateAPIView.as_view(), name = 'todo_list'),
    path('<int:pk>', api_views.TodoDetailAPIView.as_view(), name = 'todo_detail'),
]

#Function based#
# urlpatterns = [
#     path('todos/', api_views.todo_list_create, name = 'todo_list'),
#     path('todos/<int:pk>', api_views.todo_list_detail, name = 'todo_detail'),
# ]