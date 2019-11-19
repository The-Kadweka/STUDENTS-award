from django.db import models
import datetime as dt


class Student(models.Model):
    student_image = models.ImageField(upload_to = 'profile/')
    student_name=models.CharField(max_length=30)
    school_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)

    @classmethod
    def get_all_students(cls):
        students= cls.objects.all()
        return students
    @classmethod
    def search_by_full_name(cls,search_term):
        students = cls.objects.filter(full_name__icontains=search_term)
        return students

class Awards(models.Model):
    award_name = models.CharField(max_length =30)
    description = models.CharField(max_length =200)
    pub_date = models.DateTimeField(auto_now_add=True)
    student_name= models.ForeignKey(Student)

    def __str__(self):
        return self.award_name
    @classmethod
    def todays_awards(cls):
        today = dt.date.today()
        awards = cls.objects.filter(pub_date__date= today)
        return awards

    @classmethod
    def show_all(cls):
        today = dt.date.today()
        awards= cls.objects.filter(pub_date__date = today)
        return awards

    @classmethod
    def days_news(cls,date):
        awards = cls.objects.filter(pub_date__date = date)
        return awards
