from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "done", "created_at")
    list_filter = ("done",)
    search_fields = ("title",)

# Register your models here.
