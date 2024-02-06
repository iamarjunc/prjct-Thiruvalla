from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Home.html')
def thiruvalla(request):
    return render(request,'tvla.html')