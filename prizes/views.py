from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Awards,Student

# Create your views here.
def index(request):
    students = Student.get_all_students()
    awards = Awards.todays_awards()
    return render(request, 'students.html',{"students":students,'awards':awards})



def convert_dates(dates):

    # Function that gets the weekday number for the date.
     day_number = dt.date.weekday(dates)

     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
     day = days[day_number]
     return day
def search_results(request):

    if 'student' in request.GET and request.GET["student"]:
        search_term = request.GET.get("student")
        searched_students = Student.search_by_fname(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"students": searched_students})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
