from django.shortcuts import render, redirect
from .forms import TaskForm
from . import supabase_service
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    # Handle creation of new task
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            supabase_service.add_task(title)  # This creates the new todo in Supabase
            return redirect('index')  # Prevent form resubmission
    else:
        form = TaskForm()

    tasks = supabase_service.get_tasks()  # Fetch all todos from Supabase
    return render(request, 'todo/index.html', {'form': form, 'tasks': tasks})

@csrf_exempt
def delete(request, task_id):
    supabase_service.delete_task(task_id)
    return redirect('index')

@csrf_exempt
def toggle(request, task_id):
    tasks = supabase_service.get_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        supabase_service.toggle_complete(task_id, not task['completed'])
    return redirect('index')
