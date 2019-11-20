from django.shortcuts import render,redirect,get_list_or_404
from .models import Student,Award
from .forms import StudentForm,AwardForm
from django.contrib.auth.models import  User  

# Create your views here.
def home(request):
    title='Featured'
    awards=Award.objects.all()
    students=Student.objects.all()
    return render(request,'index.html',{'students':students,'title':title,'awards':'awards'})

def add_student(request):
    title = 'ADD NEW STUDENT'
    user=request.user
    if request.method=='POST':
        user = request.user
        owner =Student(owner=user)
        form = StudentForm(request.POST,request.FILES,instance=owner)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =StudentForm()
    return render (request,'student.html',{'form':form,'title':title})
        
def awards(request):
    title = 'STUDENT AWARD'
    if request.method=='POST':
        form = AwardForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=AwardForm()
    return render(request,'award.html',{'form':form,'title':title})
def my_students(request):
    title='STUDENT AVAILLABLE'
    user = request.user
    students = Student.objects.all().filter(owner__username=user)
    return render (request,'students.html',{'title':title,'students':students,'awards':'awards'})

