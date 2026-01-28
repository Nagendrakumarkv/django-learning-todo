from django.shortcuts import render
from .models import Task  # Import the model

def task_list(request):
    # 1. Fetch all tasks from the database
    tasks = Task.objects.all()

    # 2. Bundle them into a dictionary (context)
    context = {'tasks': tasks}

    # 3. Return the HTML page with the data inside
    return render(request, 'tasks/task_list.html', context)