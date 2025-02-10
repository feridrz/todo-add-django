from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])
    def completed(self, request):
        """Get all completed todos"""
        todos = Todo.objects.filter(completed=True)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending todos"""
        todos = Todo.objects.filter(completed=False)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def toggle_completed(self, request, pk=None):
        """Toggle the completed status of a todo"""
        todo = self.get_object()
        todo.completed = not todo.completed
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)
