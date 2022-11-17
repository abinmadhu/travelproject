from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Team
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    ob=Team.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})

# def task(request):
#     ob=Team.objects.all()
#     return render(request, "index.html", {"res":ob})

"""def operations(request):
    x=int(request.GET["num1"])
    y=int(request.GET["num2"])
    add=x+y
    sub=x-y
    div=x/y
    mul=x*y
    return render(request,'about.html',{"addition": add, "Difference":sub, "Division": div, "Multiplication": mul})

def contact(request):
    return render(request,'contact.html')"""