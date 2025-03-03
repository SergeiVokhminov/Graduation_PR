from django.db import models

from employees.models import Employee


class Task(models.Model):
    """Поля для модели задача."""

    TODO_STATUS = "ToDo"
    DONE_STATUS = "Done"
    CLOSED_STATUS = "Closed"

    STATUS_CHOICES = (
        (TODO_STATUS, "К исполнению"),
        (DONE_STATUS, "Выполнена"),
        (CLOSED_STATUS, "Отменена"),
    )

    title = models.CharField(
        max_length=250,
        verbose_name="Название задачи",
        help_text="Введите наименование задачи",
    )
    description = models.TextField(
        verbose_name="Описание задачи",
        help_text="Введите наименование задачи",
        null=True,
        blank=True,
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="parent",
        verbose_name="Родительская задача",
        null=True,
        blank=True,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Исполнитель задачи",
        null=True,
        blank=True,
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        verbose_name="Статус",
        help_text="Введите статус",
        null=True,
        blank=True,
    )
    deadline = models.DateField(
        verbose_name="Deadline",
        help_text="Введите срок исполнения",
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(
        default=False, verbose_name="Признак активной задачи"
    )
    is_related = models.BooleanField(
        default=False, verbose_name="Признак связанной задачи"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
