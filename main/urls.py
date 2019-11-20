from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$', views.home,name='home'),
    url(r'^award/',views.add_student, name='student'),
    url(r'^awards/',views.awards,name='awards'),
    url(r'students/',views.my_students,name='students')
]

