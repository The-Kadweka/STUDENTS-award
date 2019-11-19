from .models import Student
from django import forms
#
# class NewPostForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['likes', 'comments', 'profile']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['student_id']
