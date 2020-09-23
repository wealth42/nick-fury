from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Voice import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Voice.urls')),
    url('^$', views.main, name = 'Homepage'),
    url('Add', views.index, name = 'scriptII'),
    url('Name', views.Name, name="scriptN"),
    url('Address', views.Address, name="scriptAD"),
    url('Age', views.Age, name="scriptA"),
    url('Contact', views.Contact, name="scriptC"),
    url('Symptom', views.Symptom, name="scriptS"),
    url('Daignosis', views.Daignosis, name = 'scriptD'),
    url('Medication', views.Medication, name='scriptM'),
    url('pdf', views.pdf, name = 'scriptP'),
    url('show', views.show, name = 'scriptshow'),
    url('search',views.search, name = 'scriptsearch'),
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)