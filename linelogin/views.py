from django.shortcuts import render


# Create your views here.

def linelogins(request):
    return render(request,'linelogin/login.html')

