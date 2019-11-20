from django.conf.urls import url,include
from django.conf.urls.static import static
from  django.conf import settings
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.login, name='login'),
    url(r'^main/', include ('main.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url('^logout/',views.logout,{'next_page':'/'})
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
