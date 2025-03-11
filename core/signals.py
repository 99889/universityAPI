from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Professor, Enrollment, Assignment, Submission

@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        print(f"New student created: {instance}")

@receiver(post_save, sender=Professor)
def create_professor_profile(sender, instance, created, **kwargs):
    if created:
        print(f"New professor created: {instance}")

@receiver(post_save, sender=Enrollment)
def notify_enrollment(sender, instance, created, **kwargs):
    if created:
        print(f"New enrollment: {instance.student} in {instance.course}")

@receiver(post_save, sender=Assignment)
def notify_assignment_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New assignment created: {instance.title}")

@receiver(post_save, sender=Submission)
def notify_submission(sender, instance, created, **kwargs):
    if created:
        print(f"New submission: {instance.student} for {instance.assignment}")