from rest_framework import viewsets
from rest_framework import generics

from simple.models import Project, Task
from restapi.serializers import ProjectSerializer, TaskSerializer



class ProjectViewSet(viewsets.ModelViewSet):    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskByProjectList(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk', None)
        if project_pk is not None:
            return Task.objects.filter(project__pk=project_pk)
        return []
