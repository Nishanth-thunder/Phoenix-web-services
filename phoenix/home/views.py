from django.shortcuts import render
from .models import data
def home(request):
    return render(request, 'home/home.html')
# Create your views here.
def career(request):
    return render(request, 'home/career.html')
def new(request):
    nam=request.POST.get("name")
    rol=request.POST.get("role")
    ag= request.POST.get("age")
    loc=request.POST.get("location")
    exp=request.POST.get("experience")
    job=request.POST.get("jobrole")
    class1=request.POST.get("class12")
    cgp=request.POST.get("cgpa")
    emai=request.POST.get("email")
    dat=data(name=nam,role=rol,age=ag,location=loc,experience=exp,jobrole=job,class12=class1,cgpa=cgp,
                  email=emai)
    dat.save()
    return render(request, 'home/success.html')



