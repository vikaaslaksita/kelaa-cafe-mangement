from django.contrib import admin
from result.models import Enquiry
class Saveenquiry (admin.ModelAdmin):
    en=('name','email','phone')
admin.site.register(Enquiry,Saveenquiry)

