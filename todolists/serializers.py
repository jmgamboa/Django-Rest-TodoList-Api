from rest_framework import serializers
from todolists.models import TodoList, TodoItem
from django.contrib.auth.models import User


class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    todoitems = serializers.StringRelatedField(many=True)
    class Meta:
        model = TodoList
        fields = ('id', 'created', 'title', 'owner', 'todoitems')
    

class TodoItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    list_name = TodoListSerializer
    class Meta:
        model = TodoItem
        fields = ('id', 'created', 'title', 'done', 'trash', 'list_name', 'owner')