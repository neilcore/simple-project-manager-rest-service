# simple-project-manager-rest-service
a simple REST service project manager

==========================================
INSTALLATION
-> create a virtual environment (and activate)
-> install requirements.txt
-> run commands "makemigrations" and "migrate"
-> run project "python manage.py makemigrations"

==========================================
API endpoints
projects/ -> list of projects
projects/create/ -> create a project
projects/project/<int:pk>/ -> retrieve a single project
projects/project/update/<int:pk>/ -> update a project
projects/project/destroy/<int:pk>/ -> delete a project
projects/tasks/ -> task list
projects/tasks/task/<int:pk>/ -> retrieve a single task object
projects/tasks/create/ -> create a project task
projects/tasks/task/update/<int:pk>/ -> update a task
projects/tasks/task/destroy/<int:pk>/ -> delete a project task
