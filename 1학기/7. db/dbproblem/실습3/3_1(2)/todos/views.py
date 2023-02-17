from django.shortcuts import redirect, render
from django.urls import is_valid_path
import todos

from todos.forms import TodoForm
from .models import Todo
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.order_by('-pk')
        context = {
            'todos': todos
        }
        return render(request, 'todos/index.html', context)
    else:
        return redirect('accounts:login')
    

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')

def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == 0:
        todo.completed = 1
    else:
        todo.completed = 0
    todo.save()
    return redirect('todos:index')