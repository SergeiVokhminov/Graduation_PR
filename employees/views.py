from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
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
    """Просмотр списка сотрудников и их задачи, отсортированных по количеству активных задач."""

    def busy_employees(self, request):

        employees = Employee.objects.annotate(
            task_count=Count("tasks", filter=Q(tasks__is_active=True))
        ).order_by("task_count")

        data = []
        for emp in employees:
            active_tasks = emp.tasks.filter(is_active=True).values_list("title", flat=True)
            data.append(
                {
                    "Фамилия": emp.last_name,
                    "Имя": emp.first_name,
                    "Количество активных задач": emp.task_count,
                    "Названия активных задач": list(active_tasks),
                }
            )

        return Response(data)
