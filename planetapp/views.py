from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import PlanetModel,InformationModel,ContactInfoModel,User

# Create your views here.
def display(request):
    obj=PlanetModel.objects.all()
    con=ContactInfoModel.objects.all()

    return render(request,'index.html',{'obj':obj,'con':con})
    
''''def con_on_all_pages(request):
    return {'con':ContactInfoModel.objects.all}'''

def features(request):
    card1=InformationModel.objects.all()
    return render(request,'info.html',{'card1':card1})  

def addUser(request):
   
    if request.method=='POST':
        name=request.POST['name']
        mobileNumber=request.POST['mobileNumber']
        mail=request.POST['mail']
        userobj=User.objects.create(name=name,mobileNumber=mobileNumber,mail=mail)
        return redirect('/display')

    return render(request,'index.html')    
