# -*- coding: utf-8 -*-
from django.forms import ModelForm
from todos.models import Todo

class AddForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'text']
