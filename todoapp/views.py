from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET','POST'])
def todo_list_create(request):
    
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def todo_list_detail(request, pk):
    try:
        todo_instance = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(
            {
                'errors': {
                    'code':404,
                    'message':'Todo does not exits.' 
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
    
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = TodoSerializer(todo_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        todo_instance.delete()
        return Response(
            status= status.HTTP_204_NO_CONTENT
        )