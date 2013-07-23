from rest_framework import serializers 

from simple.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'tasks', )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task



