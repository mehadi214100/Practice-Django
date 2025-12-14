from django.shortcuts import render
from .forms import Contact

def contactus(request):

    return render(request,'contactus.html')

def viewinfo(request):
    if request.POST:
        info = request.POST
        return render(request,'viewinfo.html',context={'info':info})
    return render(request,'viewinfo.html')

def handle_uploaded_file(f):  
    with open('djangoForms/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  

def forms(request):
    if request.method == 'POST':
        form = Contact(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # handle_uploaded_file(data['document'])
            print(data)
        else:
            print("invalid data")
            
            print(form.errors) 
    else:
        form = Contact()
    return render(request, 'forms.html', context={"form": form})