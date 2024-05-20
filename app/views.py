from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic is created successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
        QLTO=Topic.objects.all()
        
        
        d={'QLTO':QLTO}
        if request.method=='POST':
             tn=request.POST['tn']
             na=request.POST.get('na')
             url=request.POST['url']
             email=request.POST['email']
             RTO=Topic.objects.get(topic_name=tn)
             WO=Webpage.objects.get_or_create(topic_name=RTO,name=na,url=url,email=email)[0]
             WO.save()
            
             return HttpResponse('webpage is created successfully')
        return render(request,'insert_webpage.html',d)


def  insert_AccessRecord(request):
    QLWO=Webpage.objects.all()
    
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        date=request.POST['date']
        au=request.POST['au']
        RWO=Webpage.objects.get(id=na)
        
        AO=AccessRecord.objects.get_or_create(name=RWO,date=date,author=au)[0]
        AO.save()

        return HttpResponse('record page is created successfully')
    return render(request,'insert_AccessRecord.html',d)
   
   
   
   
#here we are updating the records of webpage
def update_webpage(request):
      Webpage.objects.filter(topic_name='Tennis').update(email='roger345@gmail.com')
      Webpage.objects.filter(url='https://dhoni.in').update(name='Dhoni')
      QWLO=Webpage.objects.all()
      d={'QWLO':QWLO}
      return render(request,'displaywebpage.html',d)


#here we are updating records of accessrecords

def update_AccessRecord(request):
      AccessRecord.objects.filter(author='Dhoni').update(date='2023-01-02')
      AccessRecord.objects.filter(author='vidya').update(date='2002-01-07')
      QWLO=AccessRecord.objects.all()
      d={'QWLO':QWLO}
      return render(request,'display_accessrecord.html',d)








#here we are the delete the particular records of webpage

def delete_webpage(request):
      Webpage.objects.filter(topic_name='kho-kho').delete()
      
      return HttpResponse('deleted successfully')
# here we are deleting the records of accessrecord of particular record
def delete_accessrecord(request):
      AccessRecord.objects.filter(author='jh').delete()
      
      return HttpResponse('deleted successfully')



#here we are selecting multiple options by using dropdownlist
def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
         STL=request.POST.getlist('tn')#selecttopiclist
         WOS=Webpage.objects.none()
         for i in STL:
              WOS=WOS|Webpage.objects.filter(topic_name=i)
         d1={'WOS':WOS}
         return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)


#here we are selecting multiple option by using checkbox

def checkbox(request):
     QLTO=Topic.objects.all()
     d={'QLTO':QLTO}
     return render(request,'checkbox.html',d)
     