from django.shortcuts import render

from django.http import HttpResponse
import qrcode

from langdetect import detect
import speech_recognition as sr
from googletrans import Translator
from langdetect import DetectorFactory
DetectorFactory.seed = 0

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import json

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas   
from .forms import *
  
auth0user = None
userdata = None
@login_required
def dashboard(request):
    user = request.user
    global auth0user
    global userdata
    auth0user = user.social_auth.filter(provider='auth0')[0]
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': user.email,
    }

    return render(request, 'Voice/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4), 'id':'123876RFQW'
    })


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)


def speech():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    local_lang='hi'
    audio = ""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 3)
        audio = r.listen(source)
    try:
        spoken_txt = r.recognize_google(audio,language='en-US')
        print(spoken_txt)
    except:
        print("Error")
    return spoken_txt


def main(request):
    return render(request, 'Voice/main.html')

def index(request):
    return render(request,'Voice/index.html')

dat = []
for i in range(7):
    dat.append('')

dat[0] = 'Dinkar123'

def Name(request):
    data=speech()
    dat[0] = data
    return render(request,'Voice/index.html',{'data':dat})

def Address(request):
    data=speech()
    dat[1] = data
    return render(request,'Voice/index.html',{'data':dat})

def Age(request):
    data=speech()
    dat[2] = data
    return render(request,'Voice/index.html',{'data':dat})

def Contact(request):
    data=speech()
    dat[3] = data
    return render(request,'Voice/index.html',{'data':dat})

def Symptom(request):
    data=speech()
    dat[4] = data
    return render(request,'Voice/index.html',{'data':dat})


def Daignosis(request):
    data=speech()
    dat[5] = data
    return render(request,'Voice/index.html',{'data':dat})

def Medication(request):
    data=speech()
    dat[6] = data
    return render(request,'Voice/index.html',{'data':dat})

from reportlab.pdfgen import canvas   
import qrcode
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime, date

def pdf(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        symptom = request.POST.get('symptom')
        daignosis = request.POST.get('daignosis')
        medication = request.POST.get('medication')
    p = canvas.Canvas(f'{dat[0]}.pdf') 
    p.setFont("Times-Roman", 24)  
    p.drawString(400,800, "Dr. Octocat")
    p.drawString(400,775, "MBBS")
    p.drawImage("datafiles/logo.png", 45, 740, width = 100, height = 100) 
    p.setFont("Times-Roman", 18) 
    p.drawString(0,730,"_____________________________________________________________________")
    now = datetime.now()
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    current_time = now.strftime("%H:%M:%S")
    p.drawString(50, 695, f"Date : {d2}")
    p.drawString(400, 695, f"Time : {current_time}")
    p.drawString(0,680,"_____________________________________________________________________")
    p.drawString(100,650,f"Name                          :  {dat[0]}")
    p.drawString(100,620,f"Addres                        :  {dat[1]}")
    p.drawString(100,590,f"Age                             :  {dat[2]}")
    p.drawString(100,560,f"Contact No.                :  {dat[3]}")
    p.drawString(100,530,f"Symptoms                  :  {dat[4]}")
    p.drawString(100,500,f"Daignosis                   :  {dat[5]}")
    p.drawString(100,470,f"Medication                 :  {dat[6]}")
    p.drawImage("media/images/sign.png", 400,200, width = 100, height = 100)
    p.drawString(400, 180, "Doctor's Signature")
    p.showPage()  
    p.save()
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.txt")
    if gauth.credentials is None:
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("credentials.txt")  

    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title':f"{dat[0]}"})
    file.SetContentFile(f'{dat[0]}.pdf')
    file.Upload()
    result = None
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for item in file_list:
        if item['title'] == f'{dat[0]}':
            result = 'https://drive.google.com/file/d/' + item['id'] + '/view?usp=drivesdk'
            break
    qr = qrcode.QRCode()
    qr.add_data(result)
    qr.make()
    img = qr.make_image()
    img.save('assets/qrcode.png')
    return render(request, 'Voice/Last.html')

def search(request):
    return render(request, 'Voice/patient_record.html')

def show(request):
    name = None
    link = None
    if request.method == 'POST':
        print("hello")
        title = request.POST.get('title')
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("credentials.txt")
        if gauth.credentials is None:
            gauth.GetFlow()
            gauth.flow.params.update({'access_type': 'offline'})
            gauth.flow.params.update({'approval_prompt': 'force'})
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile("credentials.txt")  

        drive = GoogleDrive(gauth)

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for item in file_list:
            if item['title'] == title:
                link = 'https://drive.google.com/file/d/' + item['id'] + '/view?usp=drivesdk'
                name = item['title']
                break

    return render(request, 'Voice/patient_record.html',{'result':{'name':name, 'link':link}})

def signature_upload(request): 
    sign = None
    if request.method == 'POST': 
        form = SignatureForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save()
            if request.method == 'GET':
                sign = Signature.objects.all()  
                return render(request, 'Voice/dashboard.html',{
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4), 'id':'123876RFQW'}) 
    else: 
        form = SignatureForm() 
    return render(request, 'Voice/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4),'signature' : 'Signature Uploaded !!!','form' : form, 'id':'123876RFQW'}) 
 
