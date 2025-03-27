from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Настройки отображения модели Employee в админ-панели Django."""

    list_display = ("id", "first_name", "last_name", "position")
