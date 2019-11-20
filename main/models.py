from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.forms.fields import CharField,ImageField,ChoiceField,MultiValueField


REVIEW_CHOICES=(
    ('TURING AWARD','1'),
    ('MILLENIUM TECHNOLOGY','2'),
    ('KYOTO PRIZE','3'),
    ('IEEE MEDAL ','4')
)

class Award(models.Model):
    award_title= models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE)

    def __str__(self):
        return self.award_title

    @classmethod
    def awards(self,username):
        awards=self.objects.filter(awards__user__username=username)
        return awards

class Student(models.Model):
    owner = models.ForeignKey(User)
    image=models.ImageField(upload_to='images/')
    username = models.CharField(max_length=60)
    bio= models.CharField(max_length=250)
    awards = models.ManyToManyField('Award', related_name='student' ,blank=True)

    @classmethod
    def update(self,user):
        return self.update(user)

    def awards(self,username):
        awards=self.objects.filter(awards__user__username=username)
        return awards

    def __str__(self):
        return self.owner.username
