from rest_framework.serializers import ModelSerializer

from tasktracker.models import Task


class TaskSerializer(ModelSerializer):
    """Сериализатор модели задачи."""

    class Meta:
        model = Task
        fields = "__all__"
