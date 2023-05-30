from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Sudheer'}
    return render(request,'wish.html',context=d)
    
def conditions(request):
    c={'a':10,'b':20}
    return render(request,'conditions.html',context=c)