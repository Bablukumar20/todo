from django.shortcuts import render, redirect
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        }
    return render(request, 'home.html', context)

def addTask(request):
    if request.method == "POST":
        task_text = request.POST.get("task")
        if task_text:
            Task.objects.create(task=task_text, is_completed=False)
    return redirect('home')







