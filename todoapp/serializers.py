import datetime
from rest_framework import serializers
from todoapp.models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(max_length=100)
    todo_name = serializers.CharField(max_length=100)
    todo_date = serializers.DateField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):

        return Todo.objects.create(**validated_data)
    
    def update(self, instance ,validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.todo_name = validated_data.get('todo_name', instance.todo_name)
        instance.todo_date = validated_data.get('todo_date', instance.todo_date)
        created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance