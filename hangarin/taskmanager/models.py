from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, db_index=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Priority(models.Model):
    priority_name = models.CharField(max_length=100)

    def __str__(self):
        return self.priority_name

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

    def __str__(self):
        return self.title
    
class Note(models.Model):
    taskFK = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content

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
    
    def __str__(self):
        return self.title

