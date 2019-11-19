from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'welcome'),
    url('^prizes/',views.prizes,name = 'prizes'),
    url('^awarding/',views.awarding,name = 'awarding'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^today/$',views.awards_of_day,name='awardsToday'),
    url(r'^new/student$', views.new_student, name='new-student'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastAwards')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
