from django import forms
from .models import Student,Award

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        exclude= ['awards','owner']

class AwardForm(forms.ModelForm):
    class Meta:
        model= Award
        fields='__all__'