from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee


def home(request):
    employee = Employee.objects.all()
    print(employee)
    context = {"title": "My Django Site"}
    context = {
        'employees' : employee,
    }
    return render(request, 'home.html', context)

