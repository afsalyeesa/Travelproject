from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import places

# Create your views here.

def demo(request):
    obj=place.objects.all()
    ans=places.objects.all()
    return render(request,"index.html",{'result':obj,'results':ans})



