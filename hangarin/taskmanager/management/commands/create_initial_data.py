from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from taskmanager.models import Task, Note, SubTask, Category, Priority

class Command(BaseCommand):
    help = 'Create Initial Data for the Application'

    def handle(self, *args, **kwargs):
        self.create_task(3)
        self.create_notes(3)
        self.create_subtask(3)

    # Fake Data for Task Model
    def create_task(self, count):
        fake = Faker()

        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                categoryFK=Category.objects.order_by('?').first(),
                priorityFK=Priority.objects.order_by('?').first(),
                )
        
        self.stdout.write(self.style.SUCCESS('Initial Data for "Task" Created Successfully.'))
    
    # Fake Data for Note Model
    def create_notes(self, count):
        fake = Faker()

        for _ in range(count):
            Note.objects.create(
                taskFK=Task.objects.order_by('?').first(),
                content=fake.paragraph(nb_sentences=3),
                )

        self.stdout.write(self.style.SUCCESS('Initial Data for "Note" Created Successfully.'))
    
    # Fake Data for SubTask Model
    def create_subtask(self, count):
        fake = Faker()

        for _ in range(count):
            SubTask.objects.create(
                parentTaskFK=Task.objects.order_by('?').first(),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]))
            
        self.stdout.write(self.style.SUCCESS('Initial Data for "Subtask" Created Successfully.'))
