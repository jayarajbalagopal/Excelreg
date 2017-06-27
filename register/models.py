import random
import string
from django.db import models

# Create your models here.
def genexid(size=5,nums=string.digits):
	exid='EXLID'
	for _ in range(size):
	 exid +=random.choice(nums)
	return exid

def uniqueid():
	code=genexid()
	qs=userinfo.objects.filter(excelid=code).exists()
    	if qs:
        	uniqueid()
        return code

class userinfo(models.Model):

    class Meta:
        verbose_name = "userinfo"
        verbose_name_plural = "userinfos"

    excelid=models.CharField(max_length=10,primary_key=True,default='excel',null=False)
    name=models.CharField(max_length=100,null=True)
    college=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=50,unique=True,null=True)
    phone=models.CharField(max_length=10,null=True)
    present=models.BooleanField(default=False)
    
    def __str__(self):
    	return str(self.name)
  
    def save(self,*args,**kwargs):
    	code=uniqueid()
    	self.excelid=code
    	super(userinfo,self).save(*args,**kwargs)

