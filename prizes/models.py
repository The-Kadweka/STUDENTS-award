from django.db import models

class Awards(models.Model):
    award_name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    date = models.EmailField()
    student_awarded=models.CharField()
