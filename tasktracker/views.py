from django.db.models import Count
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employees.models import Employee
from tasktracker.models import Task
from tasktracker.serializers import TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    """Класс для создания задачи."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_task = serializer.save()
        new_task.user = self.request.user
        new_task.save()


class TaskListAPIView(ListAPIView):
    """Класс для просмотра списка всех задач."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(RetrieveAPIView):
    """Класс для просмотра информации о задаче."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(UpdateAPIView):
    """Класс для изменения задачи."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskDeleteAPIView(DestroyAPIView):
    """Класс для удаления задачи."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)


class ImportantTasksView(viewsets.ViewSet):
    """Класс для просмотра задач, которые не взяты в работу, но от которых зависят другие задачи, взятые в работу."""

    def important_tasks(self, request):

        dependent_tasks = Task.objects.filter(
            parent_task__isnull=False,
        )
        print(dependent_tasks)

        important_tasks_info = []
        for task in dependent_tasks:
            employees = Employee.objects.annotate(task_count=Count("tasks")).order_by(
                "task_count"
            )

            # Наименее загруженный сотрудник
            least_busy_employee = employees.first()
            # print(least_busy)
            available_employees = []

            for employee in employees:
                if (
                    employee != least_busy_employee
                    and employee.task_count <= least_busy_employee.task_count + 2
                ):
                    available_employees.append(employee.last_name)

            important_tasks_info.append(
                {
                    "Важная задача": task.title,
                    "Срок исполнения": task.deadline,
                    "Исполнитель": available_employees,
                }
            )

        return Response(important_tasks_info)
