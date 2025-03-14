from django.db.models import Count
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """Создание нового работника."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeListAPIView(ListAPIView):
    """Просмотр списка работников."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """Просмотр информации о работнике."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateAPIView(UpdateAPIView):
    """Редактирование информации о работнике."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyAPIView(DestroyAPIView):
    """Удаление работника."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class BusyEmployeesView(viewsets.ViewSet):
    """Просмотр сотрудников и их задач, отсортированных по количеству активных задач."""

    def busy_employees(self, request):
        employees = Employee.objects.annotate(task_count=Count("tasks")).order_by(
            "task_count"
        )
        # print(employees)
        data = [
            {
                "Фамилия": emp.last_name,
                "Имя": emp.first_name,
                "Количество активных задач": emp.task_count,
            }
            for emp in employees
        ]
        return Response(data)
