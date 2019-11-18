from django.db import models
import datetime as dt

class Awards(models.Model):
    award_name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    student_awarded=models.CharField(max_length=30)

    def __str__(self):
        return self.award_name

class Student(models.Model):
    student_image = models.ImageField(upload_to = 'profile/')
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    schoo_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    award= models.ForeignKey(Awards)

    def __str__(self):
        return self.fname
    @classmethod
    def todays_awards(cls):
        today = dt.date.today()
        students = cls.objects.filter(pub_date__date7 = today)
        return students

    @classmethod
    def days_news(cls,date):
        students = cls.objects.filter(pub_date__date = date)
        return students
