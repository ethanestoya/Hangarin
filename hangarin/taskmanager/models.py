from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, db_index=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50)

class Priority(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=50,
            choices=[("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
            ],
            default = "Pending"
            )
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE)
    priorityFK = models.ForeignKey(Priority, on_delete=models.CASCADE)

class Note(models.Model):
    taskFK = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()

class SubTask(models.Model):
    parentTaskFK = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50,
            choices=[("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
            ],
            default = "Pending"
            )


