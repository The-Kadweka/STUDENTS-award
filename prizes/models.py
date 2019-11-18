from django.db import models
import datetime as dt

class Awards(models.Model):
    award_name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    student_awarded=models.CharField(max_length=30)

    def __str__(self):
        return self.award_name
    @classmethod
    def todays_awards(cls):
        today = dt.date.today()
        awards = cls.objects.filter(pub_date__date7 = today)
        return awards

    @classmethod
    def show_all(cls):
        today = dt.date.today()
        awards= cls.objects.filter(pub_date__date = today)
        return awards

    @classmethod
    def days_news(cls,date):
        students = cls.objects.filter(pub_date__date = date)
        return students

class Student(models.Model):
    student_image = models.ImageField(upload_to = 'profile/')
    full_name=models.CharField(max_length=30)
    schoo_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    award= models.ForeignKey(Awards)

    @classmethod
    def get_all_students(cls):
        students= cls.objects.all()
        return students
    @classmethod
    def search_by_fname(cls,search_term):
        students = cls.objects.filter(fname__icontains=search_term)
        return students
