from django.db import models


class Employee(models.Model):
    """Поля для модели сотрудника."""

    first_name = models.CharField(max_length=50, verbose_name="Имя", help_text="Введите Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", help_text="Введите Фамилию")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество сотрудника:", null=True, blank=True)
    position = models.CharField(
        max_length=100,
        verbose_name="Должность",
        help_text="Укажите должность сотрудника",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
