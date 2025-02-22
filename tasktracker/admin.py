from django.contrib import admin
from tasktracker.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Настройки отображения модели Task в админ-панели Django."""

    list_display = ("id", "title", "parent_task", "employee", "status", "deadline")
