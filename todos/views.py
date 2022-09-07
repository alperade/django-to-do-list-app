from django.shortcuts import render

from todos.models import TodoList, TodoItem


def TodoListListView(request):
    context = {"todo_list_list": TodoList.objects.all()}

    return render(request, "todos/list.html", context)


def TodoListDetailView(request, pk):
    context = {"todo_list_detail": TodoList.objects.get(pk=pk)}

    return render(request, "todos/detail.html", context)
