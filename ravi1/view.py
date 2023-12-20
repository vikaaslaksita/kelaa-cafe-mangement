from django.shortcuts import render
from result.models import *
def hompage(request):

  return render(request,'welcome.html')

def value(request):
    if request.method=="POST":       
        a= request.POST.get('name')
        b= request.POST.get('email')
        c= request.POST.get('phone')
        en=Enquiry(name=a,email=b,phone=c)
        en.save()
    return render(request,"index.html")


def page2(request):
    return render(request, 'page2.html')



def page4(request):  
    return render (request, 'page4.html')

def page5(request):  
    return render (request, 'page5.html')




def images(request):
    return render(request,'image.html')




