from django.shortcuts import render

# Create your views here.

def nucleo(request):
    return render(request,'nucleo/index.html')