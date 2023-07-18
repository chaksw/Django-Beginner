from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer
# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    # def get(self, request):
    #     output = [{"id": output.id, "title": output.title, "description": output.description,
    #               "compelted": output.completed}
    #               for output in Todo.objects.all()]
    #     return Response(output)
    
    # def post(self, request):
    #     serializer = TodoSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)