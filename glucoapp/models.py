# glucoapp/models.py

from django.contrib.auth.models import User
from django.db import models

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_unit = models.CharField(max_length=10, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L')], default='mg/dL')
    target_range_min = models.FloatField(default=70)  # Valor en mg/dL o mmol/L
    target_range_max = models.FloatField(default=140)  # Valor en mg/dL o mmol/L

    def __str__(self):
        return self.user.username

class GlucoseReading(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    level = models.FloatField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.username} - {self.date} - {self.level}"

    class Meta:
        ordering = ['-date']

class UserPreferences(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    date_range_start = models.DateField(null=True, blank=True)
    date_range_end = models.DateField(null=True, blank=True)
    view_option = models.CharField(max_length=20, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily')

    def __str__(self):
        return f"{self.patient.username} Preferences"