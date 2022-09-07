from django.contrib import admin

# Register your models here.
from todos.models import (
    TodoList,
)


class TodoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
