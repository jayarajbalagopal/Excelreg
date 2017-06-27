from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from register.validators import redundantmail,validatemail

class registrationform(forms.Form):
	name=forms.CharField(max_length=50,required=True,label='',widget=forms.TextInput(attrs={
		"placeholder":"Fullname",
		"class":"form-control",
		"style":"height:50px;margin-bottom:30px;"
		}))
	college=forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={
		"placeholder":"College name",
		"class":"form-control",
		"style":"height:50px;margin-bottom:30px;"
		}))
	email=forms.EmailField(required=True,label='',validators=[redundantmail,],widget=forms.TextInput(attrs={
		"placeholder":"Email address",
		"class":"form-control",
		"style":"height:50px;margin-bottom:30px;"
		}))
	phone=forms.CharField(max_length=10,min_length=10,label='',widget=forms.TextInput(attrs={
		"placeholder":"Phone number",
		"class":"form-control",
		"style":"height:50px;"
		}))
	def clean(self):
		cleaned_data=super(registrationform,self).clean()
		print(cleaned_data)
