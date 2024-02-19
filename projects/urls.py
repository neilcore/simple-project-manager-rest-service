from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name ='home'),
    path('projects/', views.ProjectsAPIView.as_view({'get': 'list'}), name ='project-list'),
    path('projects/create/', views.ProjectsAPIView.as_view({'post': 'create'}), name="project-create"),
    path('projects/project/<int:pk>/', views.ProjectsAPIView.as_view({'get': 'retrieve'}), name ='project-retrieve'),
    path('projects/project/update/<int:pk>/', views.ProjectsAPIView.as_view({'put': 'update'}), name="project-update"),
    path('projects/project/destroy/<int:pk>/', views.ProjectsAPIView.as_view({'delete': 'destroy'}), name="project-destroy"),
    path('projects/tasks/', views.TaskAPIView.as_view({'get': 'list'}), name="task-list"),
    path('projects/tasks/task/<int:pk>/', views.TaskAPIView.as_view({'get': 'retrieve'}), name="task-retrieve"),
    path('projects/tasks/create/', views.TaskAPIView.as_view({'post': 'create'}), name="task-create"),
    path('projects/tasks/task/update/<int:pk>/', views.TaskAPIView.as_view({'put': 'update'}), name="task-update"),
    path('projects/tasks/task/destroy/<int:pk>/', views.TaskAPIView.as_view({'delete': 'destroy'}), name="task-destroy"),
]
