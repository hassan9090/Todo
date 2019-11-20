from django.shortcuts import render
from django.http import HttpResponse         # add this to use HttpResponse for testing
from rest_framework import viewsets          # add this to use viewsets from rest_framework
from .serializers import TaskSerializer      # add this to link serializer
from .models import Task,State               # add this to link models
# Create your views here.

class TaskView(viewsets.ModelViewSet):  # add this
    serializer_class = TaskSerializer  # add this
    queryset = Task.objects.all()  # add this

def index(request):
    return HttpResponse("Hello, world. You're at the task index.")
