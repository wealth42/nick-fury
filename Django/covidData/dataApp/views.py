from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

import requests
url1 =("https://api.covid19api.com/summary")
response1 = requests.get(url1).json()

url2=('https://api.covid19india.org/data.json')
response2 = requests.get(url2).json()


def home(request):
    return render(request,'dataApp/about.html')

def globalcases(request):
    globalcoData=response1["Global"]
    countriescoData=response1["Countries"]
    return render(request,'dataApp/globalCases.html',{'globalcoData':globalcoData,'countriescoData':countriescoData})
    
def countrycases(request):
    countrycoData=response2["cases_time_series"][-1]
    statescoData=response2["statewise"]
    return render(request,'dataApp/countryCases.html',{'countrycoData':countrycoData,'statescoData':statescoData})

def preventcovid(request):
    return render(request,'dataApp/prevention.html')