from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ["dept_name"]

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
