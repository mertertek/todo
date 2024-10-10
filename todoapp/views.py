from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsTodoOwner
from rest_framework.permissions import IsAuthenticated


class TodoListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            todos = Todo.objects.all()
        else:
            todos = Todo.objects.filter(user=request.user)

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class TodoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTodoOwner]

    def get_object(self, pk):
        todo_instance = get_object_or_404(Todo, pk=pk, user=self.request.user)
        return todo_instance
    
    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(data=serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = self.get_object(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






###FUNCTION METHOD###
# @api_view(['GET','POST'])
# def todo_list_create(request):
    
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
    
#     elif request.method =='POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def todo_list_detail(request, pk):
#     try:
#         todo_instance = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(
#             {
#                 'errors': {
#                     'code':404,
#                     'message':'Todo does not exits.' 
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
    
    
#     if request.method == 'GET':
#         serializer = TodoSerializer(todo_instance)
#         return Response(serializer.data)
    
#     elif request.method =='PUT':
#         serializer = TodoSerializer(todo_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method =='DELETE':
#         todo_instance.delete()
#         return Response(
#             status= status.HTTP_204_NO_CONTENT
#         )
    