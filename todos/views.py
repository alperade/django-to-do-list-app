from django.shortcuts import render, redirect

from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm


def TodoListListView(request):
    context = {"todo_list_list": TodoList.objects.all()}

    return render(request, "todos/list.html", context)


def TodoListDetailView(request, pk):
    context = {"todo_list_detail": TodoList.objects.get(pk=pk)}

    return render(request, "todos/detail.html", context)


def TodoListCreateView(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.owner = request.user
            plan.save()
            form.save_m2m()
            return redirect("todo_list_detail", pk=plan.id)
    else:
        form = TodoListForm()
    context = {"form": form}
    return render(
        request,
        "todos/create.html",
        context,
    )
