from django.db import models

class Awards(models.Model):
    award_name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    student_awarded=models.CharField(max_length=30)

    def __str__(self):
        return self.award_name

class Student(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    award= models.ForeignKey(Awards)

    def __str__(self):
        return self.fname
