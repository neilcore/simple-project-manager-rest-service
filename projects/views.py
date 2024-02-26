from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from .models import Task, Projects, STATUS_CHOICES
from rest_framework import status

from .serializers import ProjectSerializers, TaskSerializer

from django.shortcuts import get_object_or_404

import io
from rest_framework.parsers import JSONParser
    

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
            serializer = ProjectSerializers(queryset, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            queryset: Projects = Projects.objects.order_by("date_created")
            serializer = ProjectSerializers(queryset, many=True, context={'request': request})
            return Response(serializer.data)
    
    def create(self, request):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = ProjectSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f'{serializer.validated_data.get("name")} is created!'}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk = None):
        queryset: Projects = get_object_or_404(Projects, pk=pk)
        serializer = ProjectSerializers(queryset, many=False, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk = None):
        queryset = get_object_or_404(Projects, pk=pk)
        update_data = request.data
        serializer = ProjectSerializers(queryset, data=update_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Updated successfully!"})


    def destroy(self, request, pk = None):
        queryset: Projects = get_object_or_404(Projects, pk=pk)
        object_name: Projects = queryset.employee
        queryset.delete()
        return Response({"message": f'Employee schedule for {object_name} was deleted!'}, status=status.HTTP_200_OK)

class TaskAPIView(viewsets.ViewSet):
    def list(self, request):
        queryset: Task = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f'Task created!'}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset: Task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(queryset, context={'request': request})
        return Response(serializer.data)
    
    def update(self, request, pk = None):
        queryset = get_object_or_404(Task, pk=pk)
        update_data = request.data
        serializer = TaskSerializer(queryset, data=update_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Updated successfully!"})

    def destroy(self, request, pk = None):
        queryset: Task = get_object_or_404(Projects, pk=pk)
        queryset.delete()
        return Response({"message": f'Task was deleted!'}, status=status.HTTP_204_NO_CONTENT)