from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    PRIORITY_CHOICES = [
        ("URGENT", "Urgent"),
        ("HIGH", "High"),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
    ]
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default="LOW"
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    def __str__(self):
        return self.name
