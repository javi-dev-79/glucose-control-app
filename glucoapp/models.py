# glucoapp/models.py

from django.contrib.auth.models import User
from django.db import models


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_unit = models.CharField(
        max_length=10,
        choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
        default="mg/dL",
    )
    target_range_min = models.FloatField(default=70)  # Value in mg/dL or mmol/L
    target_range_max = models.FloatField(default=140)  # Value in mg/dL or mmol/L

    def __str__(self):
        return self.user.username


class GlucoseReading(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)  # Change to False to allow editing
    level = models.FloatField()
    notes = models.TextField(blank=True, null=True)
    test_type = models.CharField(
        max_length=100,
        choices=[
            ('puncture', 'Punción de dedo'),
            ('blood', 'Análisis de sangre'),
            # Add more test types as necessary
        ],
        default='punctura_dedo',  # Default value
        null=True,  # You can leave it as null=True if you want to allow null values
        blank=True  # So that it is not required in the form
    )
    location = models.CharField(max_length=50, choices=[('home', 'Casa'), ('hospital', 'Hospital')], blank=True, null=True)
    medium_used = models.CharField(max_length=100, blank=True, null=True)  # Optional field

    def __str__(self):
        return f"{self.patient.username} - {self.date} - {self.level}"


class UserPreferences(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    date_range_start = models.DateField(null=True, blank=True)
    date_range_end = models.DateField(null=True, blank=True)
    view_option = models.CharField(
        max_length=20,
        choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")],
        default="daily",
    )

    def __str__(self):
        return f"{self.patient.username} Preferences"
