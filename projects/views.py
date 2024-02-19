from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Task, Projects, STATUS_CHOICES

from .serializers import ProjectSerializers, TaskSerializer

from django.shortcuts import get_object_or_404
    

@api_view(['GET'])
def homeView(request):
    return Response({"message": "A simple project manager by briancore22"})
    
class StatusChoiceAPIView(viewsets.ViewSet):
    def get(self, request, format=None):
        return Response(STATUS_CHOICES)
    
    def post(self, request, format=None):
        pass
    
class ProjectsAPIView(viewsets.ViewSet):
    def list(self, request):
        if request.GET:
            filter_queries = {}
            if request.GET.get("name"):
                filter_queries.update({"name__iexact": request.GET.get("name")})
            if request.GET.get("description"):
                filter_queries.update({"description__icontains": request.GET.get("description")})
            if request.GET.get("status"):
                filter_queries.update({"status__icontains": request.GET.get("status")})
            if request.GET.get("date_finished"):
                filter_queries.update({"date_finished": request.GET.get("date_finished")})
            
            queryset: Projects = Projects.objects.filter(**filter_queries).order_by("date_created")
            serializer = ProjectSerializers(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset: Projects = Projects.objects.order_by("date_created")
            serializer = ProjectSerializers(queryset, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        pass
    
    def retrieve(self, request, pk = None):
        queryset: Projects = get_object_or_404(Projects, pk=pk)
        serializer = ProjectSerializers(queryset, many=False)
        return Response(serializer.data)

    def update(self, request, pk = None):
        pass

    def destroy(self, request, pk = None):
        queryset: Projects = get_object_or_404(Projects, pk=pk)
        object_name: Projects = queryset.name
        queryset.delete()
        return Response({"message": f'Project {object_name} was deleted!'})

class TaskAPIView(viewsets.ViewSet):
    def list(self, request):
        queryset: Task = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset: Task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk = None):
        pass

    def destroy(self, request, pk = None):
        pass