from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Sudheer'}
    return render(request,'wish.html',context=d)
    
def conditions(request):
    c={'a':110,'b':20,'c':40}
    return render(request,'conditions.html',context=c)

def loop(request):
    s={'name':'SUDHEER'}
    return render(request,'loop.html',s)