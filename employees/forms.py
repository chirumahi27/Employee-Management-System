from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "email", "phone", "salary", "joining_date", "department"]
        widgets = {
            "joining_date": forms.DateInput(attrs={"type": "date"}),
            "salary": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
        }

    def clean_salary(self):
        salary = self.cleaned_data["salary"]
        if salary < 0:
            raise forms.ValidationError("Salary cannot be negative.")
        return salary
