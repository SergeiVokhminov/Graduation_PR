from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employees.models import Employee
from tasktracker.serializers import TaskSerializer


class EmployeeSerializer(ModelSerializer):
    """Сериализатор модели работника."""

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeTaskSerializer(TaskSerializer):
    """Сериализатор модели для подсчета активных задач работника."""

    tasks = TaskSerializer(many=True, read_only=True)
    active_tasks_count = SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            "id",
            "first_name",
            "last_name",
            "position",
            "tasks",
            "active_tasks_count",
        )

    def get_active_tasks_count(self, obj):
        """Возвращает количество активных задач у работника."""

        return obj.tasks.filter(status="start").count()
