from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import generics
from todolists.serializers import TodoListSerializer, TodoItemSerializer
from models import TodoList, TodoItem
from permissions import CustomPermissions, IsOwnerOrReadOnly


class TodoListView(generics.ListCreateAPIView):
    """
    View and Create single Todo Lists
    """
    serializer_class = TodoListSerializer
    permission_classes =(IsOwnerOrReadOnly, )
 
    def get_queryset(self):
        """
        Associate the Todo Lists with the logged in user        
        """
        owner = self.request.user.id
        return TodoList.objects.filter(owner_id=owner)
    def perform_create(self, serializer):
        """
        Create the Todo Lists given user        
        """
        serializer.save(owner=self.request.user)


class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Creates read/write/update/delete for each item
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes =(IsOwnerOrReadOnly, )

class TodoItemView(generics.ListCreateAPIView):
    """
    View all and create single Todo Items
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = (CustomPermissions, )

    def get_queryset(self):
        """
        Associate the Todo Lists with the logged in user        
        """
        owner = self.request.user.id
        return TodoItem.objects.filter(owner_id=owner)
    def perform_create(self, serializer):
        """
        Create the Todo Lists given user        
        """
        serializer.save(owner=self.request.user)


class TodoItemSingleView(generics.RetrieveUpdateDestroyAPIView):
    """
    Creates read/write/update/delete for each item
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes =(IsOwnerOrReadOnly, )


def index(request):
    context = ''
    return render_to_response('todolist.html', context, context_instance=RequestContext(request))













