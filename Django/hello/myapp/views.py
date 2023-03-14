from django.shortcuts import render,HttpResponse


# Create your views here.

def index (request):
    context={

          "variable":"this is data form variable"

    }
    return render(request,'index.html',context)

def about (request):
    return HttpResponse("I am in aboutpage")
