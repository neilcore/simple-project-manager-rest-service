from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('P', 'Pending'),
    ('A', 'Active'),
    ('PRC', 'Processing'),
    ('D', 'Done'),
    ('C', 'Cancelled'),
    ('IAC', 'Inactive'),
    ('PSPN', 'Posponed'),
    ('WRK', 'Working')
)

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="P")

    def __str__(self) -> str:
        return f'{self.name}'
    

    class Meta:
        verbose_name_plural = "Projects"

class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_started = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    total_hours = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="P")


    def __str__(self) -> str:
        return f'{self.project.name} - {self.name}'
    

    class Meta:
        verbose_name_plural = "Tasks"