from django.utils import timezone
from rest_framework.test import APITestCase

from employees.models import Employee
from tasktracker.models import Task
from users.models import User


class TaskTestCase(APITestCase):
    """Тесты для задач."""

    def setUp(self):
        """Подготовка исходных данных для тестов.
        Создает тестовую задачу для последующих запросов."""

        # Создаем тестового пользователя для добавления сотрудников и задач
        self.user = User.objects.create(
            email="test@test.com",
            first_name="Test",
            last_name="Test",
            phone_number="+79222222222",
            is_active=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)

        # Создаем исполнителя для тестирования
        self.employee = Employee.objects.create(
            first_name="Иван",
            last_name="Иванов",
            patronymic="Иванович",
            position="Тестировщик",
        )

        # Создаем задачу для тестирования
        self.task = Task.objects.create(
            title="Тест",
            description="Тестовая задача.",
            employee=self.employee,
            status="free",
            deadline=timezone.now().date() + timezone.timedelta(days=7),
            owner=self.user,
            is_active=True,
        )

    def test_task_creation(self):
        """Тест создания задачи."""

        self.assertEqual(self.task.title, "Тест")
        self.assertEqual(self.task.description, "Тестовая задача.")
        self.assertEqual(self.task.employee, self.employee)
        self.assertEqual(self.task.status, "free")
        self.assertTrue(self.task.is_active)
        self.assertEqual(self.task.owner, self.user)

    def test_task_list(self):
        """Тест вывода списка задач."""

        response = self.client.get("/tasktracker/list/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тест")

    def test_task_detail(self):
        """Тест вывода подробной информации о задаче."""

        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Тест")
        self.assertEqual(task.description, "Тестовая задача.")
        self.assertEqual(task.employee, self.employee)
        self.assertEqual(task.status, "free")
        self.assertTrue(task.is_active)
        self.assertEqual(task.owner, self.user)

    def test_task_update(self):
        """Тест изменения задачи."""

        self.task.title = "Обновление тестов"
        self.task.save()

        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, "Обновление тестов")

    def test_task_deletion(self):
        """Тест удаления задачи."""

        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task.id)
