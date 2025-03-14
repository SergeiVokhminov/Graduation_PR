from rest_framework.serializers import ModelSerializer

from employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    """Сериализатор модели работника."""

    class Meta:
        model = Employee
        fields = "__all__"
