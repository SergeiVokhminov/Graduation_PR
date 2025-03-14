from django.urls import path

from tasktracker.apps import TasktrackerConfig
from tasktracker.views import (ImportantTasksView, TaskCreateAPIView,
                               TaskDeleteAPIView, TaskListAPIView,
                               TaskRetrieveAPIView, TaskUpdateAPIView)

app_name = TasktrackerConfig.name

urlpatterns = [
    path("create/", TaskCreateAPIView.as_view(), name="task_create"),
    path("list/", TaskListAPIView.as_view(), name="task_list"),
    path("detail/<int:pk>/", TaskRetrieveAPIView.as_view(), name="task_detail"),
    path("update/<int:pk>/", TaskUpdateAPIView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteAPIView.as_view(), name="task_delete"),
    path(
        "important/",
        ImportantTasksView.as_view({"get": "important_tasks"}),
        name="task_important",
    ),
]
