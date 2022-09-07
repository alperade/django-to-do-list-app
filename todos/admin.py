from django.contrib import admin

# Register your models here.
from todos.models import (
    TodoList,
    TodoItem,
)


class TodoListAdmin(admin.ModelAdmin):
    pass


class TodoItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem, TodoItemAdmin)
