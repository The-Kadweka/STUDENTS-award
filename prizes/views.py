from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Awards,Student

# Create your views here.
def index(request):
    students = Student.get_all_students()
    return render(request, 'students.html',{"students":students})



def convert_dates(dates):

    # Function that gets the weekday number for the date.
     day_number = dt.date.weekday(dates)

     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
     day = days[day_number]
     return day
