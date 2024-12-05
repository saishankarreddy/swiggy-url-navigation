from django.shortcuts import render

# Create your views here.
def chicken(request):
    return render(request,'chicken.html')