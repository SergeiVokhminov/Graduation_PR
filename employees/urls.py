from django.urls import path

from employees.apps import EmployeesConfig
from employees.views import (BusyEmployeesView, EmployeeCreateAPIView,
                             EmployeeDestroyAPIView, EmployeeListAPIView,
                             EmployeeRetrieveAPIView, EmployeeUpdateAPIView)

app_name = EmployeesConfig.name

urlpatterns = [
    path("create/", EmployeeCreateAPIView.as_view(), name="employee_create"),
    path("list/", EmployeeListAPIView.as_view(), name="employee_list"),
    path("detail/<int:pk>/", EmployeeRetrieveAPIView.as_view(), name="employee_detail"),
    path("update/<int:pk>/", EmployeeUpdateAPIView.as_view(), name="employee_update"),
    path("delete/<int:pk>/", EmployeeDestroyAPIView.as_view(), name="employee_delete"),
    path(
        "busy_employees/",
        BusyEmployeesView.as_view({"get": "busy_employees"}),
        name="busy_employees",
    ),
]
