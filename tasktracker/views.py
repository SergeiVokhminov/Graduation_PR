from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

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
