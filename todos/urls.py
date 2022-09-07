from django.urls import path

from todos.views import (
    TodoListListView,
)

urlpatterns = [
    path("", TodoListListView, name="todo_list_list"),
]
