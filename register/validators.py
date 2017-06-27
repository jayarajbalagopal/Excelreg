from django.core.exceptions import ValidationError
from register.models import userinfo
from django.core.validators import EmailValidator
from validate_email import validate_email

def redundantmail(value):
	qs_exists=userinfo.objects.filter(email=value).exists()
	if qs_exists:
		raise ValidationError("This mail id is aldready registered.")
	else:
		return value

def validatemail(value):
	is_valid = validate_email(value,verify=True)
	if is_valid:
		return value
	raise ValidationError("Enter a valid email address.")
    
