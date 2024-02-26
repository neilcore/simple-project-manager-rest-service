from rest_framework import serializers
from .models import Projects, Task

class ProjectSerializers(serializers.ModelSerializer):
    detail_view = serializers.HyperlinkedIdentityField(view_name="project-retrieve")
    date_created = serializers.DateTimeField(read_only=True, format="%B %d, %Y %H:%M %p")
    date_finished = serializers.DateField(read_only=True, format="%B %d, %Y")
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="task-retrieve"
    )
    class Meta:
        model = Projects
        fields = [
            "pk", "name", "description", "date_created", "date_finished",
            "status", "detail_view", "tasks"
        ]

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.StringRelatedField(source="project", read_only=True)
    detail_view = serializers.HyperlinkedIdentityField(view_name="project-retrieve")
    date_created = serializers.DateTimeField(read_only=True, format="%B %d, %Y %H:%M %p")
    date_started = serializers.DateField(read_only=True, format="%B %d, %Y")
    total_hours = serializers.IntegerField(read_only=True)
    class Meta:
        model = Task
        fields = [
            'pk', 'name', 'project', 'project_name', 'description', 'date_created',
            'date_started', 'status', 'start_time', 'end_time', 'total_hours', 'detail_view'
        ]

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.project = validated_data.get('project', instance.project)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance