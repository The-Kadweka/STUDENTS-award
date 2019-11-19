from .models import Student,Awards
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['student_id']

class AwardsForm(forms.ModelForm):
    class Meta:
        model = Awards
        exclude = ['award_id']
