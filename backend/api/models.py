from django.db import models

class HealthcareProfessional(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    location = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
