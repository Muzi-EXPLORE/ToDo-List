# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from todos.models import Todo
from todos.forms import AddForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {'todos': todos }
    return render(request, 'todos/index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {'todo': todo }
    return render(request, 'todos/details.html', context)

def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddForm()
        context = {'form': form }
        return render(request, 'todos/add.html', context)