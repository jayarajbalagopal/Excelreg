from django.contrib import admin
from register.models import userinfo
from controlroom.models import venue,event
# Register your models here.

admin.site.register(userinfo)
admin.site.register(venue)
admin.site.register(event)