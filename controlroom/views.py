from django.shortcuts import render
from django.views.generic import TemplateView
from controlroom.models import venue,event
from register.models import userinfo
from django.http import JsonResponse




class ControlRoomView(TemplateView):
	def get(self,request,*args,**kwargs):
		context={
		"title":"testing",
		}
		return render(request,"controlroom.html",context)

	
	def post(self,request,*args,**kwargs):
		error1=False
		error2=False
		result=[]
		sb=-1
		searchby=request.POST.get('searchby')
		value=request.POST.get('value')



		if request.POST.get('ajax'):
			ajax=request.POST.get('ajax')
			if(ajax=="venue"):
				list1=venue.objects.values_list('venue_id',flat=True)
			elif(ajax=="eventname"):
				list1=event.objects.values_list('event_name',flat=True)
			elif(ajax=="excelid"):
				list1=userinfo.objects.values_list('excelid',flat=True)
			d=[]
			for li in list1:
				li.replace("u","")
				d.append(li)
			data = {
			'dataset':d
			}
			return JsonResponse(data)



		if((searchby=="" or searchby==None) and (value=="Not Applicable" or value=="")):
			error1=True
		if((searchby=="venue" or searchby=="eventname" or searchby=="excelid") and value==""):
			error2=True
			
		if(searchby=="venue"):
			result=venue.objects.filter(venue_id=value)
			sb=0
		elif(searchby=="eventname"):
			result=event.objects.filter(event_name__iexact=value.upper())
			sb=1
		elif(searchby=="excelid"):
			result=userinfo.objects.filter(excelid=value)
			sb=2
		elif(searchby=="unoccupied venues"):
			result=venue.objects.filter(occupied=False)
			sb=0
			value="Not Applicable"
		elif(searchby=="ongoing events"):
			result=event.objects.filter(status=1)
			sb=1
			value="Not Applicable"
		elif(searchby=="completed events"):
			result=event.objects.filter(status=2)
			sb=1
			value="Not Applicable"
		context={
		"title":"testing",
		"searchby":searchby,
		"value":value,
		"error1":error1,
		"error2":error2,
		"searchby_num":sb,
		"obj":result,
		"len":len(result)
		}
		return render(request,"controlroom.html",context)
