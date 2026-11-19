from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm
from .models import Department, Employee


def employee_list(request):
    employees = Employee.objects.select_related("department").all()
    query = request.GET.get("q", "").strip()
    department_id = request.GET.get("department", "").strip()

    if query:
        employees = employees.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
            | Q(phone__icontains=query)
        )

    if department_id.isdigit():
        employees = employees.filter(department_id=int(department_id))

    context = {
        "employees": employees,
        "departments": Department.objects.all(),
        "query": query,
        "selected_department": department_id,
    }
    return render(request, "employees/employee_list.html", context)


def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm()

    return render(request, "employees/employee_form.html", {
        "form": form,
        "page_title": "Add Employee",
        "submit_label": "Add Employee",
    })


def employee_update(request, id):
    employee = get_object_or_404(Employee, pk=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employees/employee_form.html", {
        "form": form,
        "page_title": "Edit Employee",
        "submit_label": "Save Changes",
        "employee": employee,
    })


def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)

    if request.method == "POST":
        employee_name = employee.name
        employee.delete()
        messages.success(request, f"{employee_name} was deleted successfully.")
        return redirect("employee_list")

    return render(request, "employees/employee_confirm_delete.html", {
        "employee": employee,
    })
