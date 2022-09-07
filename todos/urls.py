from django.urls import path

from todos.views import TodoListListView, TodoListDetailView, TodoListCreateView

urlpatterns = [
    path("", TodoListListView, name="todo_list_list"),
    path("<int:pk>/", TodoListDetailView, name="todo_list_detail"),
    path("create/", TodoListCreateView, name="todo_list_create"),
]
