from django.db import models

class Incident_report(models.Model):  # <-- Must inherit from models.Model
    incident_report_number = models.CharField(max_length=255)
