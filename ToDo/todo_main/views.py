from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def addTask(request):
    if request.method == "POST":
        task = request.POST.get("task")
        # You can save to DB here later
        return HttpResponse(f"Task added: {task}")
    return redirect("home")