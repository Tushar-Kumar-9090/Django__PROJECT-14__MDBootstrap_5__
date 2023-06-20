from django.shortcuts import render

# Create your views here.

def mdboot(request):
    return render(request, 'mdboot.html')

def mdb5_courosal(request):
    return render(request, 'mdb5_courosal.html')