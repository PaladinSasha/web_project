from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from tasks.models import Project, Task


# Create your models here.
class BugReport(models.Model):
    STATUS_CHOISES = (
        ('New', 'Новая'),
        ('In progress', 'В работе'),
        ('Completed', 'Завершена')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bugReports',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bugReports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='New'
    )
    priority = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOISES = (
        ('In progress', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='features',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='features',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='In progress'
    )
    priority = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)