#Importing modules
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
import requests
import json
import requests
from bs4 import BeautifulSoup

# Create your views here.

#HOME page function
def home(request):
    #For Corona rotating box
    list_cols = []
    #Page from Corona's count is coming
    URL = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/' 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser') #Using BeautifulSoup to extract data from URL
    #Extracting table data
    table = soup.find("table", { "id" : "table3" })
    table_body=table.find('tbody')
    rows = table_body.find_all('tr')
    #Extracting top 4 rows of the table
    for row, row in zip(range(4), rows):
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        list_cols.append(cols)
    #Each row in dictionary with different key value    
    context = {}
    context['DATA1'] = list_cols[0]
    context['DATA2'] = list_cols[1]
    context['DATA3'] = list_cols[2]
    context['DATA4'] = list_cols[3]
    return render(request, "coronaupdate.html", context) #Rendering to the coronaupdate.html page
    #return render(request, "base.html")

#India's News Function
def india(request):
    #API Request with ApiKey
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    #Loading JSON data
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {"api":api}) #Rendering dictionary to index.html page

#Australia's News Function
def australia(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=au&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {"api":api})

#Canada's News Function
def canada(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=ca&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content) 
    return render(request, "index.html", {"api":api})

#New Zealand's News Function
def new_zealand(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=nz&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {"api":api})

#Singapore's News Function
def singapore(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=sg&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {"api":api})

#US's News Function
def us(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {"api":api})

#Entertainment's News Function
def entertainment(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {'api':api})

#Health's News Function
def health(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {'api':api})

#Science's News Function
def science(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {'api':api})

#Sports's News Function
def sports(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {'api':api})

#Technology's News Function
def tech(request):
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=be2dc2d8e68d421d99bc2bcc73102489")
    api = json.loads(news_api_request.content)
    return render(request, "index.html", {'api':api})

