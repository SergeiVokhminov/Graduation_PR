from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

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
