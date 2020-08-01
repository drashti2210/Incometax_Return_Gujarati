from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from income_tax.views import *
from income_tax.templates import *
from income_tax.models import *
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from selenium import webdriver
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import win32api
import random 
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
from pymsgbox import *
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
def itr2(req):
    return render(req,'itr2.html')
def feedbackform(request):
	f=request.POST
	print(f)
	subject, from_email, to = 'FEED BACK', settings.EMAIL_HOST_USER,"dhwanipopat2000@gmail.com"
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p>'
	msg = EmailMultiAlternatives(subject, json.dumps(f), from_email, [to])
	msg.send()
	
	return render(request,'home1.html')
def itr21(request):
			
	c={}
	c.update(csrf(request))
	uname=request.POST.get("name")
	print(uname)
	income=int(request.POST.get("income"))
	year=int(request.POST.get("year"))
	Net_Tax_income=0
	if income<=250000:
		Net_Tax_income=0
		print("a")
	elif income>250000 and income<=500000:
		k=12500
		Net_Tax_income=k
		print("a1")
	elif income>500000 and income<=750000:
		k=int((income-500000)*0.1)+12500
		Net_Tax_income=k
		print("a2")
	elif income>750000 and income<=1000000:
		k=int((income-750000)*0.15)+12500+25000
		print("a3")
		Net_Tax_income=k
	elif income>1000000 and income<=1250000:
		k=int((income-1000000)*0.2)+12500+25000+37500
		Net_Tax_income=k
		print("a4")
	elif income>1250000 and income<=1500000:
		k=int((income-125000)*0.25)+12500+25000+37500+50000
		Net_Tax_income=k
		print("a5")
	elif income>1500000:
		k=int((income-100000)*0.25)+12500+25000+37500+50000+62500
		Net_Tax_income=k
		print("a6")
	else:
		Net_Tax_income=0
		print("fghjk")
	Net_Tax_income+=Net_Tax_income*0.04
	user=Itr21(Id2=uname,income=income,Year=year,Net_Tax_income=Net_Tax_income)
		
	user.save()

	user=UserInfo.objects.filter(UserId=uname)
	for user in user:
		xx=user.Email

	subject, from_email, to = 'YOUR INCOME TAX CALCULATION', settings.EMAIL_HOST_USER,xx
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p><table border="1"><tr><td>Name</td><td>'+uname+'</td></tr><tr><td>Net income tax</td><td>'+str(Net_Tax_income)+'</td></tr></table>'
	msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
	msg.content_subtype = "html" 
	msg.send()
	print(Net_Tax_income)
	
	return render(request,'final_calculation.html',{"username":uname,"k":Net_Tax_income})


def index(request):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	m = cv2.VideoCapture(0)
	rec=cv2.face.LBPHFaceRecognizer_create()
	rec.read("../trainningData.yml")
	id=0
	font = cv2.FONT_HERSHEY_SIMPLEX
	sampleNum = 0;
	while (True):
		ret, img = m.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 4)
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
			cv2.putText(img, "recognized", (x, y - 10), font, 0.55, (0, 255, 0), 1)
		cv2.imshow('Face', img)
		cv2.waitKey(0)
		if (cv2.waitKey(1)==ord('q')):
			break
	m.release()
	cv2.destroyAllWindows()

def cgi(request):
	c={}
	c.update(csrf(request))
	

	f = open("abc.txt", "w")
	print(gs.translate('hello world', 'de'))

	a=str(request.POST.get('first_name'))
	b=str(request.POST.get('last_name'))
	
	print(a)
	f.write
	f.write(a)
	f.write(b)

	f.close()

#open and read the file after the appending:
	f = open("abc.txt", "r")
	print(f.read())
	return render(request,'cgi.html',c)
	
def new_registration(request):
		c={}
		c.update(csrf(request))
		return render(request,'registration.html',c)
def itr1form1(request):
		c={}
		c.update(csrf(request))
		return render(request,'itr1form.html',c)

def updateIn(request):
		c={}
		c.update(csrf(request))
		name=request.session['username']
		print("hhahahahhahahahahhahahahahahhhahahahaha")
		print(name)	
		view_data= UserInfo.objects.filter(UserId=name)
		x=view_data[0].UseImage
		print(x.url)
		context={'view_data':view_data,'pic':x.url}
		return render(request,'updateIn.html',context)
def home(request):
		c={}
		c.update(csrf(request))
		return render(request,'home1.html',c)
def home1(request):
		c={}
		username=request.session['username']
		is_user=False
		print('is user: ',is_user)
		if username is not None:
			is_user=True
		else:
			is_user=False
		c.update(csrf(request))
		return render(request,'home1.html',c)

def profile2(request):
		c={}
		c.update(csrf(request))
		name=request.session['username']
		print("hhahahahhahahahahhahahahahahhhahahahaha")
		print(name)	
		view_data= UserInfo.objects.filter(UserId=name)
		x=view_data[0].UseImage
		print(x.url)
		context={'view_data':view_data,'pic':x.url}
		return render(request,'profile.html',context)
def change_password1(request):
		return render(request,'change_password.html')

def change_password(request):
		c={}
		c.update(csrf(request))
		username=request.POST.get('name')
		print(username)
		s1=UserInfo.objects.get(UserId=username)
		print(s1.Email)
		r1 = random.randint(1000, 10000) 
		s=User1.objects.get(UserId=username)
		s.Password=str(r1)
		s.save()
		alert(text='YOUR NEW PASSWORD IS SENT TO YOU VIA EMAIL', title='CHANGE OF PASSWORD', button='OK')
		subject, from_email, to = 'YOUR NEW PASSWORD', settings.EMAIL_HOST_USER,s1.Email
		text_content = str(r1)
		html_content = '<p>This is an <strong>important</strong> message.</p>'
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.send()

		return  HttpResponseRedirect('/income_tax/login')


def UpdateInfo(request):
			
		c={}
		c.update(csrf(request))
		username=request.session['username']
		x=request.FILES['uploadFromPC']
		
		s=UserInfo.objects.get(UserId=username)
		s.FirstName=request.POST.get('fname')
		s.LastName=request.POST.get('lname')
		s.Contact=request.POST.get('phno')
		s.Email=request.POST.get('email')
		s.UseImage=request.FILES['uploadFromPC']
		s.save()
		return  HttpResponseRedirect('/income_tax/profile2')


def useinfo1(request):
	c={}
	c.update(csrf(request))
	return render(request,'useinfo.html',c)

def useinfo(request):
		c={}
		c.update(csrf(request))
		print("kjfdjghkfjdhljk;")
		
		username=request.session['username']
		print("skjfhkjlsdh")
		print(request.POST.get('phno'))
		print(username)
		print(request.FILES['uploadFromPC'])
		user=UserInfo(UserId=username,
					Email=request.POST.get('email'),	
					PAN=request.POST.get('pan'),
					Aadhar=request.POST.get('aadhar'),
					FirstName=request.POST.get('name')	
					,LastName=request.POST.get('surname')	
					,Contact=request.POST.get('phno')
					,UseImage=request.FILES['uploadFromPC'])
		
		user.save()
		request.session['username']=username
		return  HttpResponseRedirect('/income_tax/profile2')

def itr1form(request):
		c={}
		c.update(csrf(request))
		username = request.session['username']
		#request.session['username']=username
		user=UserInfo.objects.filter(UserId=username)
		for user in user:
			xx=user.Email
			xy=user.Aadhar
			yz=user.PAN
			xz=user.Contact
		print(username)
		file1=username
		file2=username+"11"
		f2="C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/"
		#hallo welt
		f = open(f2 + file1+".txt", "w",encoding="utf-8")
		g = open(f2 +file2+".txt", "w")
		translator = Translator()
		a=username
		a1 = translator.translate(username, src='gu', dest='en')
		g.write(a1.text)
		f.write("Pan:")
		f.write(yz)
#gs = goslate.Goslate()
		g.write("\n")
		f.write("\n")
		f.write("Aadhar:")
		f.write(xy)
		b=user.Aadhar
		b1 = translator.translate(b, src='gu', dest='en')
		g.write(b1.text)
		#g.write(gs.translate(b, 'gu'))
		g.write("\n")
		f.write(b)
		f.write("\n")
		f.write("Name:")
		f.write(str(request.POST.get('name')))
		c1 = translator.translate(str(request.POST.get('name')), src='gu', dest='en')
		g.write(c1.text)
		f.write("\n")

#		c=str(request.POST.get('Text4'))	

#		f.wirte(c)
		f.write("\n")
		f.write("Email:")
		f.write(xx)
		
		f.write("\n")
		#d1 = translator.translate(str(request.POST.get('email')), src='gu', dest='en')
		#g.write(d1.text)	
		#g.write(gs.translate(str(request.POST.get('email')), 'gu'))
		#g.write("\n")
		f.write("Phno:")
		f.write(xz)
		f.write("\n")
		#e1 = translator.translate(xz, src='gu', dest='en')
		g.write(xz)
		#g.write(gs.translate(str(request.POST.get('phno')), 'gu'))
		#g.write(gs.translate(str(request.POST.get('r1')), 'gu'))
		#g.write("\n")
		#g.write(gs.translate(str(request.POST.get('r2')), 'gu'))
		#g.write("\n")
		f.write("no:")
		f.write(str(request.POST.get('no')))
		f.write("\n")
		
		#g.write(gs.translate(str(request.POST.get('no')), 'gu'))
		#g.write("\n")
		f.write("Date1:")
		f.write(str(request.POST.get('date1')))
		f.write("\n")
		
		#g.write(gs.translate(str(request.POST.get('date1')), 'gu'))
		#g.write("\n")
		f.write("Date2:")
		f.write(str(request.POST.get('date2')))
		f.write("\n")
		
		#g.write(gs.translate(str(request.POST.get('date2')), 'gu'))
		#g.write("\n")
		#g.write(gs.translate(str(request.POST.get('r4')), 'gu'))
		#g.write("\n")
		f.close()
		pdfkit.from_file(f2 + file1 + ".txt", f2+file1+".pdf")	 
		g.close()
		pdfkit.from_file(f2 + file2+".txt", f2 + file2+".pdf") 

#open and read the file after the appending:
		f = open("abc.txt", "r")
		print(f.read())
		
		screenshot = pyautogui.screenshot()
		screenshot.save("screen.png")
		#grabzIt = GrabzItClient.GrabzItClient("MDBiMDJlMWU4MmNhNGVjYzg5ZTk0Y2JhODY3YjMxOGY=", "Bz8/Pz8/Umc8Xz8iPz89PxQ/Pz9KKyM/Rz9UPys/Pz8=")
		#options = GrabzItImageOptions.GrabzItImageOptions()
		#options.format = "jpg"

		#grabzIt.URLToImage("C:\Users\DHWANI\Desktop\incometax\income_tax\templates\in, options)
# Then call the Save or SaveTo method
		#grabzIt.SaveTo("result11.jpg")
		#password=request.POST.get('password')
		#pdfkit.from_string(request.POST.get('Text1'),'GfG.pdf') 		
	#	pdfkit.from_file(r'C:\Users\DHWANI\Desktop\incometax\income_tax\templates\itr1form.html', 'outmy.pdf') 

		return render(request,'itr1dform.html',{"username" : username})


def registration(request):
		username=request.POST.get('eid')
		password=request.POST.get('password')
		#name=request.POST.get('name')
		#email=request.POST.get('email')
		user=authenticate(username=username,password=password)
		if user is None:
			user=User.objects.create_user(username,password)
			user.save()
			auth.login(request,user)
			s=User1(UserId=username,Password=password)
			s.save()
			request.session['username']=username
			return HttpResponseRedirect('/income_tax/useinfo1',{"username":username})
		else:
			return HttpResponseRedirect('/income_tax/home1')

def itr1dform1(request):
		c={}
		c.update(csrf(request))
		return render(request,'itr1dform.html')

def show(request):	
		c={}
		c.update(csrf(request))
		username=request.session['username']
		view_data= Itr21.objects.filter(Id2=username)

		view_data1= income_Ded.objects.filter(UserId=username)
		print(view_data1)
		context={'view_data1':view_data1,'view_data':view_data}
		return render(request,'show.html',context)
def delete(request, id):  
    employee = income_Ded.objects.get(id=id)  
    employee.delete()  
    return HttpResponseRedirect("/income_tax/show")  
def delete1(request, id):  
    employee = Itr21.objects.get(id=id)  
    employee.delete()  
    return HttpResponseRedirect("/income_tax/show")  

def itr1dform(request):
	if request.session['is_user']:
		UserId=request.session['username']
		kp=request.POST.get('kp')
		Pro_Tax=request.POST.get('Pro_Tax') 	
		Trans_Allow=request.POST.get('Trans_Allow') 	
		HBA_Intr=request.POST.get('HBA_Intr') 	
		Mediclaim=request.POST.get('Mediclam') 	
		P_H_Ded=request.POST.get('P_H_Ded') 	
		Donation=request.POST.get('Donation') 	
		Other_Ded=request.POST.get('Other_Ded') 	
		Other_income=request.POST.get('Other_income') 	
		GPF_Contr=request.POST.get('GPF_Contr') 	
		State_Gvt_Ins=request.POST.get('State_Gvt_Ins') 	
		Repay_HBA=request.POST.get('Repay_HBA') 	
		NSC_Purchase=request.POST.get('NSC_Purchase') 	
		PPF=request.POST.get('PPF') 	
		LIC_Prem=request.POST.get('LIC_Prem') 	
		PLI_Prem=request.POST.get('PLI_Prem') 	
		Edu_Fee=request.POST.get('Edu_Fee') 	
		JSA=request.POST.get('JSA') 	
		Infra_Bond=request.POST.get('Infra_Bond') 	
		Equity_Link=request.POST.get('Equity_Link') 	
		Other_Eligible=request.POST.get('Other_Eligible')
		#Total_Ded=request.POST.get('Total_Ded') 	
		Total_Income=request.POST.get('Total_Income') 	
		#Net_Tax_income=request.POST.get('Net_Tax_income')
		x=int(request.POST.get('Total_Incom')) 	
		m2=x
		file1=UserId
		file2=UserId+"11"

		Total_Ded=int(kp)+int(Pro_Tax)+int(Trans_Allow)+int(HBA_Intr)+int(Mediclaim)+int(P_H_Ded)+int(Donation)+int(Other_Ded)
		x=x-Total_Ded
		print(x)
		m1=int(State_Gvt_Ins)+int(GPF_Contr)+int(Repay_HBA)+int(NSC_Purchase)+int(PPF)+int(LIC_Prem)+int(PLI_Prem)+int(Edu_Fee)+int(JSA)+int(Infra_Bond)+int(Equity_Link)+int(Other_Eligible)
		print(m1)
		if m1>150000:
			m1=150000
		else:
			m1=m1
		print(m1)
		x=x-m1
		print(x)
		l=x
		if l%10!=0:
			l=10-l%10
		x=x+l
		#print(x+l)
		k=0
		if x>500000 and x<1000000:
			k=int((x-500000)*0.2)+12500

		elif x>250000 and x<=500000:
			k=12500
		if x>1000000:
			k=(	x*0.3-1000000)+12500+100000
		#print(k)
		Net_Tax_income=int(k+int(k*0.04))
		k=Net_Tax_income
		print(Net_Tax_income)
		#print(m2-x)
		#print("hrlll"+Net_Tax_income)
		s=income_Ded(UserId=UserId,
		Pro_Tax=Pro_Tax,
		Trans_Allow=Trans_Allow, 	
		HBA_Intr=HBA_Intr, 	
		Mediclaim=Mediclaim, 	
		P_H_Ded=P_H_Ded, 	
		Donation=Donation,
		Other_Ded=Other_Ded,
		Other_income=Other_income,
		GPF_Contr=GPF_Contr,
		State_Gvt_Ins=State_Gvt_Ins,
		Repay_HBA=Repay_HBA,
		NSC_Purchase=NSC_Purchase,
		PPF=PPF,
		LIC_Prem=LIC_Prem,
		PLI_Prem=PLI_Prem,
		Edu_Fee=Edu_Fee,
		JSA=JSA,
		Infra_Bond=Infra_Bond, 	
		Equity_Link=Equity_Link, 	
		Other_Eligible=Other_Eligible, 	
		Total_Ded=Total_Ded, 	
		Total_Income=Total_Income ,
		Net_Tax_income=Net_Tax_income)
		print(s)
		s.save()
		request.session["k"] = k
		m=request.session["k"]
		string1=""
		user=UserInfo.objects.filter(UserId=UserId)
		for user in user:
			xx=user.Email

		subject, from_email, to = 'YOUR INCOME TAX CALCULATION', settings.EMAIL_HOST_USER,xx
		text_content = 'CALCULATED TAX'+str(Net_Tax_income)
		html_content = '<p>This is an <strong>important</strong> message.</p>'
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		
		msg.attach_file('C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/'+file1+".pdf")
		msg.attach_file('C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/'+file2+".pdf")

		msg.send()

		return render(request,'final_calculation.html',{"username":UserId,"k":k})

	else:
		return render(request,'home1.html')

def itr1bform1(request):
		c={}
		c.update(csrf(request))
		return render(request,'itr1bform.html')

def welcome(request):
		c={}
		c.update(csrf(request))
		return render(request,'welcome.html')

def itr1bform(request):

	if request.session['is_user']:
		userid=request.session['username']
		#username = request.session['username']
		print(userid)
		file1=userid
		file2=userid+"11"
		#password=request.POST.get('password')
		year=request.POST.get('year')
		month=request.POST.get('month')
		#total_income=request.POST.get('total_income')
		gross_salary=request.POST.get('gross_salary')
		professional_tax=request.POST.get('professional_tax')
		group_ins=request.POST.get('group_ins')
		gpf=request.POST.get('gpf')
		hba=request.POST.get('hba')
		service_ded=request.POST.get('service_ded')
		pli=request.POST.get('pli')
		lic=request.POST.get('lic')
		trans_allow=request.POST.get('trans_allow')
		first_half_ded=request.POST.get('first_half_ded')
		second_half_ded=request.POST.get('second_half_ded')
		hra_diff=request.POST.get('hra_diff')
		trans_exp=request.POST.get('trans_exp')
		ppf=request.POST.get('ppf')
		month_ded=request.POST.get('month_ded')
		da_diff=request.POST.get('da_diff')
		print(da_diff)
		#total_income=
		f = open("C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/"+file1+".txt", "a",encoding="utf-8")
		string1="\n"+userid+"\n"+year+"\n"+month+"\n"+gross_salary+"\n"+professional_tax+"\n"+group_ins+"\n"+gpf+"\n"+hba+"\n"+service_ded+"\n"+pli+"\n"+lic+"\n"+trans_allow+"\n"+first_half_ded+"\n"+second_half_ded+"\n"+hra_diff+"\n"+trans_exp+ppf+"\n"+month_ded+"\n"+da_diff
		
		f.write(string1)
		f.close()
		translator = Translator()
		
		string2="\n"+userid+"\n"+year+"\n"+month+"\n"+gross_salary+"\n"+professional_tax+"\n"+group_ins+"\n"+gpf+"\n"+hba+"\n"+service_ded+"\n"+pli+"\n"+lic+"\n"+trans_allow+"\n"+first_half_ded+"\n"+second_half_ded+"\n"+hra_diff+"\n"+trans_exp+ppf+"\n"+month_ded+"\n"+da_diff
			
		a1 = translator.translate(string2, src='gu', dest='en')
		
		g = open("C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/"+file2+".txt", "a")
		g.write(a1.text)
		g.close()
		pdfkit.from_file('C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/'+file1+".txt", 'C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/'+file1+".pdf")	 
		pdfkit.from_file('C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/'+file2+".txt", 'C:/Users/DHWANI/Desktop/proj_final/incometax/income_tax/static/income_tax/'+file2+".pdf") 
		s=income(UserId=userid,Year=year,
		Month=month,Gross_Salary=gross_salary,Professional_Tax=professional_tax,Group_Ins=group_ins,
		Gpf=gpf,Hba=hba,
		Service_Ded=service_ded,
		PLI=pli,
		LIC=lic,
		Trans_Allow=trans_allow,		Month_Ded=month_ded,
		first_half_ded=first_half_ded,
		second_half_ded=second_half_ded,		DA_Diff=da_diff,
		HRA_Diff=hra_diff,
		Trans_Exp=trans_exp,
		PPF=ppf)
		print(s)
		s.save()
		return render(request,'itr1dform.html')
	else:
		return render(request,'home1.html')
		
		
def login(request):
		c={}
		c.update(csrf(request))	
		if request.user.is_authenticated:
			return HttpResponseRedirect('/income_tax/home1')
		else:
			return render(request,'login.html')

def auth_view(request):
	#is_user=False
	#user1 = request.user
	#print(user1)
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user=authenticate(username=username ,password=password)
		print(user)
		if user:
			auth.login(request,user)
			request.session['username'] = username
			request.session['is_user']=username
			print(request.user.is_superuser)
			return render(request,'home1.html',{"username" : username,"is_user" : username})
		else:
			if request.method == 'POST':
				username1 = request.POST['username']
				password1 = request.POST['password']

				userd= User1.objects.filter(UserId=username1,Password=password1).exists()
				if userd is True:
					print(userd)
					request.session['username'] = username
					request.session['is_user']=userd
					return render(request,'home1.html',{"username" : username,"is_user" : userd}) 
				else:
					print("dfghjk")
					alert(text='CHECK USERNAME OR PASSWORD', title='SOMETHING IS WRONG', button='OK')# <-
					return render(request,'home1.html')

			return HttpResponseRedirect('/income_tax/login')
		
	#if request.method == 'POST':
	#	username = request.POST['username']
	#	password = request.POST['password']

	#	user1=authenticate(username=username ,password=password)

	#	print(username)
	#	userd= User1.objects.filter(UserId=username,Password=password).exists()
	#	print(user1)
		
	#	print("idiot")
	#	print(request.user1.is_superuser)

	#	if userd is True:
	#		print(userd)
	#		request.session['username'] = username
	#		request.session['is_user']=userd
	#		return render(request,'home1.html',{"username" : username,"is_user" : userd}) 
	#	else:
	#		print(userd)
	#		return render(request,'home1.html')"""

def loggedin(request):
    return render('loggedin.html', {"full_name": request.user.username})

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'home1.html')
		
def all_data1(request):
		c={}
		c.update(csrf(request))
		return render(request,'all_data.html')
def try1(request):
		c={}
		c.update(csrf(request))
		return render(request,'try1.html')

def all_data(request):
		print("IN ALL DATA")
		top_data=request.session['k']
		print(top_data)
		#sub_data={"s_name":cname}
		#print(sub_data)
		context={'top_data':top_data}
		return render(request,'all_data.html',context)



