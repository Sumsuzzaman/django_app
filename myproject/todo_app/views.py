from django.shortcuts import render
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == "true":
        tasks = tasks.filter(completed=True)
    elif completed == "false":
        tasks = tasks.filter(completed=False)
   
    return render(request, "task_list.html", {"tasks": tasks})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "task_detail.html", {"task": task})