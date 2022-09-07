from django.urls import path

from todos.views import (
    TodoListListView,
    TodoListDetailView,
    TodoListCreateView,
    TodoListUpdateView,
    TodoListDeleteView,
    TodoItemCreateView,
    TodoItemUpdateView,
)

urlpatterns = [
    path("", TodoListListView, name="todo_list_list"),
    path("<int:pk>/", TodoListDetailView, name="todo_list_detail"),
    path("create/", TodoListCreateView, name="todo_list_create"),
    path("<int:pk>/edit/", TodoListUpdateView, name="todo_list_update"),
    path("<int:pk>/delete/", TodoListDeleteView, name="todo_list_delete"),
    path("items/create/", TodoItemCreateView, name="todo_item_create"),
    path("items/<int:pk>/edit/", TodoItemUpdateView, name="todo_item_update"),
]
