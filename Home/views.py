from django.shortcuts import render
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})
