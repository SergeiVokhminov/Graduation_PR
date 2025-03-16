from rest_framework.test import APITestCase

from employees.models import Employee


class EmployeeTestCase(APITestCase):
    """Тесты для сотрудников."""

    def setUp(self):
        """Подготовка исходных данных для тестов.
        Создает тестового сотрудника для последующих запросов."""

        self.employee = Employee.objects.create(
            first_name="Иван",
            last_name="Иванов",
            patronymic="Иванович",
            position="Тестировщик",
        )

    def test_employee_create(self):
        """Тест создания нового сотрудника."""

        employee = Employee.objects.create(
            first_name="Петр",
            last_name="Петров",
            patronymic="Петрович",
            position="Программист",
        )
        self.assertEqual(employee.first_name, "Петр")
        self.assertEqual(employee.last_name, "Петров")
        self.assertEqual(employee.patronymic, "Петрович")
        self.assertEqual(employee.position, "Программист")
        self.assertTrue(isinstance(employee, Employee))

    def test_list_employees(self):
        """Тест получения списка сотрудников."""

        employees = Employee.objects.all()
        self.assertIn(self.employee, employees)
        self.assertEqual(employees.count(), 1)

    def test_employee_detail(self):
        """Тест получения подробной информации о сотруднике."""

        employee = Employee.objects.get(id=self.employee.id)
        self.assertEqual(str(employee), "Иванов Иван - Тестировщик")
        self.assertEqual(employee.first_name, "Иван")
        self.assertEqual(employee.last_name, "Иванов")
        self.assertEqual(employee.patronymic, "Иванович")
        self.assertEqual(employee.position, "Тестировщик")

    def test_update_employee(self):
        """Тест изменения информации о сотруднике."""

        self.employee.position = "Старший тестировщик"
        self.employee.save()

        updated_employee = Employee.objects.get(id=self.employee.id)
        self.assertEqual(updated_employee.position, "Старший тестировщик")

    def test_delete_employee(self):
        """Тест удаления сотрудника."""

        employee_id = self.employee.id
        self.employee.delete()

        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(id=employee_id)
