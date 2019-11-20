from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.forms.fields import CharField,ImageField,ChoiceField,MultiValueField



class Award(models.Model):
    award_title= models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    badge = models.ImageField(upload_to='budge')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.award_title
    def __int__(self):
        return self.pub_date
    def __binary__(self):
        return self.badge

    @classmethod
    def awards(self,username):
        awards=self.objects.filter(awards__user__username=username)
        return awards

class Student(models.Model):
    owner = models.ForeignKey(User)
    image=models.ImageField(upload_to='images/')
    username = models.CharField(max_length=60)
    school = models.CharField(max_length=30)
    bio= models.CharField(max_length=250)
    award = models.ForeignKey(Award)

    @classmethod
    def update(self,user):
        return self.update(user)

    def awards(self,username):
        awards=self.objects.filter(awards__user__username=username)
        return awards

    def __str__(self):
        return self.owner.username
