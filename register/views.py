from django.shortcuts import render
from django.views.generic import TemplateView
from register.forms import registrationform
from register.models import userinfo
import pyqrcode
import sys

class regview(TemplateView):
	def get(self,request,*args,**kwargs):
		form=registrationform()
		context={
		"title":"testing",
		"form":form
		}
		return render(request,"home.html",context)

	def post(self,request,*args,**kwargs):
		form=registrationform(request.POST)
		context={
		"title":"testing",
		"form":form
		}
		if form.is_valid():
			mail=form.cleaned_data.get('email')
			name=form.cleaned_data.get('name')
			phone=form.cleaned_data.get('phone')
			college=form.cleaned_data.get('college')
			u=userinfo(name=name,college=college,email=mail,phone=phone)
			u.save()
			obj=userinfo.objects.get(email=mail)
			im=pyqrcode.create(obj.excelid)
			im.svg('static/qrcodes/%s.svg'%(obj.excelid),scale=20)
			return render(request,"success.html",{"object":obj})
            # im=pyqrcode.create(obj.excelid)
            # im.svg('static/qrcodes/%s.svg'%(obj.excelid), scale=20)  
            # return render(request,"success.html",{"object":obj})

		return render(request,"home.html",context)