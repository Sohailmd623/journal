from django.shortcuts import render, redirect
from .models import Todo
from .forms import *


def home(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"todos": todos, "form": form}
    return render(request, 'todo/home.html', context)


def edit(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todo/edit.html', context)


def delete(request, pk):
     task= Todo.objects.get(id=pk)

     if request.method == "POST":
         task.delete()
         return redirect('/')
     context = {"task": task}
     return render(request, 'todo/delete.html', context)