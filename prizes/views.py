from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .forms import StudentForm,AwardsForm
import datetime as dt
from .models import Awards,Student

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    students = Student.get_all_students()
    awards = Awards.todays_awards()
    print(date)
    return render(request, 'students.html',{'date': date,"students":students,'awards':awards})



def awards_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def search_results(request):

    if 'student' in request.GET and request.GET["student"]:
        search_term = request.GET.get("student")
        searched_students = Student.search_by_full_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"students": searched_students})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def prizes(request):
    return render(request,'prize.html')

@login_required(login_url='/accounts/login/')
def awarding(request):
    current_user = request.user
    if request.method == 'POST':
        form = AwardsForm(request.POST, request.FILES)
        if form.is_valid():
            award = form.save(commit=False)
            award.Awards = current_user
            award.save()
        return redirect('welcome')

    else:
        form = AwardsForm()
    return render(request, 'new_student.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_student(request):
    current_user = request.user
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.student = current_user
            student.save()
        return redirect('welcome')

    else:
        form = StudentForm()
    return render(request, 'new_student.html', {"form": form})

@login_required(login_url='/accounts/login/')
def StudentProfile(request, user_id):
    student_object = get_object_or_404(Student, pk=student_id)
    if request.student == student_object:
        return redirect('profile')
    return render(request, 'profile.html', locals())
