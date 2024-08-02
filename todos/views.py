from django.shortcuts import render, redirect
from .models import *
from .forms import TodoForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def todosView(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    form = TodoForm()
    todos = Todo.objects.all()
    todoCount = len(todos)
    context = {
        'todos': todos,
        'todoCount': todoCount,
        'form': form
    }
    return render(request, 'todos.html', context)

def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos')

def contactView(request):
    return render(request, 'contact.html')