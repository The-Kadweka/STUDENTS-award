from .models import Profile
from django import forms
#
# class NewPostForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['likes', 'comments', 'profile']

class NewsProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']
