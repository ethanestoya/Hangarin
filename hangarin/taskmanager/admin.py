from django.contrib import admin
from .models import Category, Priority, Task, Note, SubTask

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("priority_name",)
    search_fields = ("priority_name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title",
                    "status",
                    "deadline",
                    "categoryFK",
                    "priorityFK",
                    )
    list_filter = ("status",
                   "priorityFK",
                   "categoryFK",
                   )
    search_fields = ("title",
                     "description",)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("taskFK",
                    "content",
                    "created_at",
                    )
    list_filter = ("created_at",)
    search_fields = ("content",)

@admin.register(SubTask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ("title",
                    "status",
                    "parentTaskFK",
                    )
    list_filter = ("status",)
    search_fields = ("title",)