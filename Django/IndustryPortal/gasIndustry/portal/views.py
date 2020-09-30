from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DCBILL, GSTBILL, NORMALBILL
import time
import smtplib
import os
from operator import itemgetter 
from datetime import date
from time import gmtime, strftime   
import datetime
today = date.today()
system_date = today.strftime("%Y-%m-%d")
current_time = datetime.datetime.now()

print(system_date,'SDSDSDDD',current_time)


def home(request):
    return render(request, 'portal/admin/dashboard.html')


def Dashboard(request):
    return render(request, 'portal/admin/dashboard.html')  

def NormalBill(request):
    return render(request, 'portal/admin/normalbill.html')

def EvaluateNormalBill(request):
    if request.POST:
        company_name=request.POST.get('company_name')
        phone_no=request.POST.get('phone_no')
        gst_no=request.POST.get('gst_no')
        oxy_cyl=request.POST.get('oxy_cyl')
        nitro_cyl=request.POST.get('nitro_cyl')
        nitro_pure_cyl=request.POST.get('nitro_pure_cyl')
        argon_cyl=request.POST.get('argon_cyl')
        da_cyl=request.POST.get('da_cyl')
        lpg_cyl=request.POST.get('lpg_cyl')
        hydrogen_cyl=request.POST.get('hydrogen_cyl')
        co2_cyl=request.POST.get('co2_cyl')
        ammonia_cyl=request.POST.get('ammonia_cyl')
        description=request.POST.get('description')

        billno='xyz'

        today = date.today()
        system_date = today.strftime("%Y-%m-%d")

        normalbill=NORMALBILL(BILLNO=billno,DATE=system_date,COMPANYNAME=company_name,PHONENO=phone_no,GSTNO=gst_no,NO_OXYEN_CYL=oxy_cyl,
        NO_NIT_CYL=nitro_cyl,NO_NIT_PURE=nitro_pure_cyl,NO_ARGON_CYL=argon_cyl,NO_DA_CYL=da_cyl,NO_LPG_CYL=lpg_cyl,
        NO_HYD_CYL=hydrogen_cyl,NO_CO2_CYL=co2_cyl,NO_AMMO_CYL=ammonia_cyl,DESCRIPTION=description)
        normalbill.save()
        if ammonia_cyl:
            print('kdkjfjbdk',ammonia_cyl)
        return render(request, 'portal/admin/qnormalbill.html')

def DcBill(request):
    return render(request, 'portal/admin/dcbill.html')

def EvaluateDcBill(request):
    if request.POST:
        company_name=request.POST.get('company_name')
        phone_no=request.POST.get('phone_no')
        gst_no=request.POST.get('gst_no')
        oxy_cyl=request.POST.get('oxy_cyl')
        nitro_cyl=request.POST.get('nitro_cyl')
        nitro_pure_cyl=request.POST.get('nitro_pure_cyl')
        argon_cyl=request.POST.get('argon_cyl')
        da_cyl=request.POST.get('da_cyl')
        lpg_cyl=request.POST.get('lpg_cyl')
        hydrogen_cyl=request.POST.get('hydrogen_cyl')
        co2_cyl=request.POST.get('co2_cyl')
        ammonia_cyl=request.POST.get('ammonia_cyl')
        description=request.POST.get('description')
        
        billno='xyz'

        today = date.today()
        system_date = today.strftime("%Y-%m-%d")

        dcbill=DcBill(BILLNO=billno,DATE=system_date,COMPANYNAME=company_name,PHONENO=phone_no,GSTNO=gst_no,NO_OXYEN_CYL=oxy_cyl,
        NO_NIT_CYL=nitro_cyl,NO_NIT_PURE=nitro_pure_cyl,NO_ARGON_CYL=argon_cyl,NO_DA_CYL=da_cyl,NO_LPG_CYL=lpg_cyl,
        NO_HYD_CYL=hydrogen_cyl,NO_CO2_CYL=co2_cyl,NO_AMMO_CYL=ammonia_cyl,DESCRIPTION=description,)
        dcbill.save()

    return redirect('/')

def GstBill(request):
    return render(request, 'portal/admin/gstbill.html')

def EvaluateGstBill(request):
    if request.POST:
        company_name=request.POST.get('company_name')
        phone_no=request.POST.get('phone_no')
        gst_no=request.POST.get('gst_no')
        oxy_cyl=request.POST.get('oxy_cyl')
        nitro_cyl=request.POST.get('nitro_cyl')
        nitro_pure_cyl=request.POST.get('nitro_pure_cyl')
        argon_cyl=request.POST.get('argon_cyl')
        da_cyl=request.POST.get('da_cyl')
        lpg_cyl=request.POST.get('lpg_cyl')
        hydrogen_cyl=request.POST.get('hydrogen_cyl')
        co2_cyl=request.POST.get('co2_cyl')
        ammonia_cyl=request.POST.get('ammonia_cyl')
        description=request.POST.get('description')

        billno='xyz'

        today = date.today()
        system_date = today.strftime("%Y-%m-%d")

        gstbill=GSTBILL(BILLNO=billno,DATE=system_date,COMPANYNAME=company_name,PHONENO=phone_no,GSTNO=gst_no,NO_OXYEN_CYL=oxy_cyl,
        NO_NIT_CYL=nitro_cyl,NO_NIT_PURE=nitro_pure_cyl,NO_ARGON_CYL=argon_cyl,NO_DA_CYL=da_cyl,NO_LPG_CYL=lpg_cyl,
        NO_HYD_CYL=hydrogen_cyl,NO_CO2_CYL=co2_cyl,NO_AMMO_CYL=ammonia_cyl,DESCRIPTION=description,)
        gstbill.save()
    return redirect('/')

def SearchByBillno(request):
    return render(request, 'portal/admin/search-bill.html')


def SearchByCylinderno(request):
        return render(request, 'portal/admin/search-cylinder.html')

def SearchByDate(request):
        return render(request, 'portal/admin/search-date.html')

def SearchByCustomer(request):
        return render(request, 'portal/admin/search-customer.html')


def EditPermanentCustomer(request):
    pass

def EditTemporaryCustomer(request):
    pass

def ExistingCustomer(request):
    pass


def AddCustomer(request):
    return render(request, 'portal/admin/addcustomer.html')
    

def DeleteAccount(request):
    pass