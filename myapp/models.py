from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    PROJECT_TYPES = [
        ('numbers', 'Numbers'),
        ('shapes', 'Shapes'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    name = models.CharField(
        max_length=100
    )

    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES,
        default='numbers'
    )

    image = models.ImageField(
        upload_to='projects/'
    )

    result = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} ({self.project_type})"