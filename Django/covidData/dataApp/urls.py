from django.urls import path,include
from dataApp import views


urlpatterns=[
    path('', views.home, name="home"),
    path('globalcovidcases/',views.globalcases,name="globalcovidcases"),
    path('countrycovidcases/',views.countrycases,name="countrycovidcases"),
    path('preventionfromcovid/',views.preventcovid,name="preventionfromcovid"),
]