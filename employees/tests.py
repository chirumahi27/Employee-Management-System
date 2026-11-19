from django.test import TestCase
from django.urls import reverse
from .models import Department, Employee


class EmployeePagesTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(
            dept_name="IT",
            location="Bangalore",
        )
        self.employee = Employee.objects.create(
            name="Test Employee",
            email="test@example.com",
            phone="9876543210",
            salary="30000.00",
            joining_date="2026-10-01",
            department=self.department,
        )

    def test_employee_list_page(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Employee")

    def test_create_form_page(self):
        response = self.client.get(reverse("employee_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Employee")

    def test_update_form_page(self):
        response = self.client.get(reverse("employee_update", args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Employee")

    def test_delete_confirmation_page(self):
        response = self.client.get(reverse("employee_delete", args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete Employee")
