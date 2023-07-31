from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'RISHI','age':14,'hobbies':['singing','playing']}
    return render(request,'data_render.html',context=d)


def conditions(request):
    d={'a':300,'b':150}
    return render(request,'conditions.html',context=d)