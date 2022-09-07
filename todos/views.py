from django.shortcuts import render

from todos.models import TodoList, TodoItem


def TodoListListView(request):
    context = {"todo_list_list": TodoList.objects.all()}

    return render(request, "list.html", context)
