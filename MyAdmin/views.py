from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from MyAdmin.views import *
from MyAdmin.templates import *
from MyAdmin.models import *
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from selenium import webdriver
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives



import pandas as pd
from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItClient
from googletrans import Translator
import numpy as np
import urllib
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pdfkit
import pyautogui 
import cgi, cgitb
import cv2
import os
from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def Form_View(req):
    return render(req,'generate.html')

def Save(request):
    print("in savvee")
    
    print(request.GET['temp'])
    data = request.GET.get('temp','')
    y = json.loads(data)
    f = Form(Description="Demo8")
    f.save()
    print("form saved")
    print(y)
    l=[]
    for k in y:
        l.append(y[k])
    print(l)
    for i in range(0,len(l),3):
        t = Textfield(name=l[i],typ=l[i+2],Label=l[i+1],form=f)
        t.save()
    return JsonResponse({'status':"success"})

def showforms(req):
    data=Form.objects.filter(Id=8)
    context={
        'forms':data,
    }
	
    return render(req,'showform.html',context=context)

def detailform(req):
    id = req.GET['id']
    f = Form.objects.get(Id=id)
    data = Textfield.objects.filter(form__pk=f.Id)
    #data = f.textfield_set.all()
    print(data)
    context={
        'alldata':data,
    }
    return render(req,'detailform.html',context=context)

def show2form(req):
    f = Form.objects.last() 
    return render(req,'showform.html',{'forms':f})
def feedbackform(request):
	f=request.POST
	print(f)
	subject, from_email, to = 'FEED BACK', settings.EMAIL_HOST_USER,"goStudy2021@gmail.com"
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p>'
	msg = EmailMultiAlternatives(subject, json.dumps(f), from_email, [to])
	msg.send()
	
	return render(request,'home1.html')
