# glucoapp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PatientProfile

@receiver(post_save, sender=User)
def create_or_update_patient_profile(sender, instance, created, **kwargs):
    if created:
        PatientProfile.objects.create(user=instance)
    else:
        try:
            instance.patientprofile.save()
        except PatientProfile.DoesNotExist:
            PatientProfile.objects.create(user=instance)
