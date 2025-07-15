import re
from django.shortcuts import redirect, render

# Create your views here.

from .forms import Studentform
from .models import Student

def home(request):
    if request.method=="POST":
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form=Studentform()
        data_std=Student.objects.all()
    return render(request,'home.html',{'data_std':data_std,'form':form})
    
def success(request):
    return render(request,"success.html")

