from django.shortcuts import render

def contactus(request):

    return render(request,'contactus.html')

def viewinfo(request):
    if request.POST:
        info = request.POST
        return render(request,'viewinfo.html',context={'info':info})
    return render(request,'viewinfo.html')

def forms(request):
    return render(request,'forms.html')