from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("dept_name", "location")
    search_fields = ("dept_name", "location")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "salary", "joining_date", "department")
    list_filter = ("department", "joining_date")
    search_fields = ("name", "email", "phone")
