from django.core.management import call_command
from django.core.management.base import BaseCommand

from tasktracker.models import Task


class Command(BaseCommand):
    """Очистка базы данных задач и загрузка сохраненных ранее данных из фикстур в базу данных."""

    help = "Заполнить базу данных задач из фикстур."

    def handle(self, *args, **kwargs):
        """Функция очистки базы данных и заполнения."""
        Task.objects.all().delete()

        call_command("loaddata", "fixture/task_fixture.json")
        self.stdout.write(self.style.SUCCESS("Фикстуры задач успешно загружены."))
