from rest_framework import serializers
from .models import Projects, Task

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.StringRelatedField(source="project", read_only=True)
    class Meta:
        model = Task
        fields = ['pk', 'name', 'project', 'project_name', 'description', 'status']