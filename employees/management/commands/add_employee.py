from django.core.management import call_command
from django.core.management.base import BaseCommand

from employees.models import Employee


class Command(BaseCommand):
    """Очистка базы данных сотрудников и загрузка сохраненных ранее данных из фикстур в базу данных."""

    help = "Заполнить базу данных сотрудников из фикстур."

    def handle(self, *args, **kwargs):
        """Функция очистки базы данных и заполнения."""
        Employee.objects.all().delete()

        call_command("loaddata", "fixture/employee_fixture.json")
        self.stdout.write(self.style.SUCCESS("Фикстуры сотрудников успешно загружены."))
