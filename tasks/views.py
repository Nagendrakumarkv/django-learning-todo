from django.shortcuts import render, redirect  # <--- Import redirect
from .models import Task
from .forms import TaskForm  # <--- Import your new Form

def task_list(request):
    # 1. Fetch all tasks from the database
    tasks = Task.objects.all()

    # 2. Bundle them into a dictionary (context)
    context = {'tasks': tasks}

    # 3. Return the HTML page with the data inside
    return render(request, 'tasks/task_list.html', context)

def create_task(request):
    # 1. If the user clicked "Submit" (POST request)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to the Database
            return redirect('task_list')  # Go back to the homepage

    # 2. If the user just visited the page (GET request)
    else:
        form = TaskForm() # Create an empty form

    # 3. Send the form (empty or with errors) to the template
    return render(request, 'tasks/task_form.html', {'form': form})