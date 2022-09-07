from django.urls import path

from todos.views import (
    TodoListListView,
    TodoListDetailView,
    TodoListCreateView,
    TodoListUpdateView,
    TodoListDeleteView,
)

urlpatterns = [
    path("", TodoListListView, name="todo_list_list"),
    path("<int:pk>/", TodoListDetailView, name="todo_list_detail"),
    path("create/", TodoListCreateView, name="todo_list_create"),
    path("<int:pk>/edit/", TodoListUpdateView, name="todo_list_update"),
    path("<int:pk>/delete/", TodoListDeleteView, name="todo_list_delete"),
]
