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
        QLTO=Topic.objects.filter(topic_name='cricket')
        QLTO=Topic.objects.filter(topic_name='Ludo')
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
    QLWO=Webpage.objects.filter(name='Dhoni')
    
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