from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"nav/home.html")

def first(request):
    return render(request,"nav/first.html")

def second(request):
    return render(request,"nav/second.html")
