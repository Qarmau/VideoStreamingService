from django.shortcuts import render
from .models import Film

def index(request):
    video=Film.objects.all()
    return render(request,'core/index.html',{'video':video})
    
