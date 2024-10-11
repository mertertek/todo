from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['user','todo_name', 'todo_date','created_at']


admin.site.register(Todo, TodoAdmin)