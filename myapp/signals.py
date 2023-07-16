from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from myapp.models import StudentProfile

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.studentprofile.save()
