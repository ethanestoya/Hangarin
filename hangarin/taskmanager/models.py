from django.db import models
from django.utils import timezone

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now,)
    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name.title()

class Priority(BaseModel):
    priority_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.priority_name.title()

class Task(BaseModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    deadline = models.DateField()
    status = models.CharField(max_length=50,
            choices=[("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
            ],
            default = "Pending"
            )
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE)
    priorityFK = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.title.title()
    
class Note(BaseModel):
    taskFK = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content.title()

class SubTask(BaseModel):
    parentTaskFK = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50,
            choices=[("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
            ],
            default = "Pending"
            )
    
    def __str__(self):
        return self.title.title()

