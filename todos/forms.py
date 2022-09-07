from django import forms

from todos.models import TodoList


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["name"]


class TodoListDeleteForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = []
