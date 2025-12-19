from django.shortcuts import render
from .forms import HackathonRegistrationForm
import os
from django.conf import settings

def handle_file(file):
    upload_path = os.path.join(settings.MEDIA_ROOT, 'resumes', file.name)
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    with open(upload_path,'wb+') as des:
        for chunk in file.chunks():
            des.write(chunk)


def hackathon(request):

    if request.method == 'POST':
        form = HackathonRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            file = data.get('resume')
            handle_file(file)
            print(data)
    else:    
        form = HackathonRegistrationForm()
    context = {
        'form':form,
    }
    return render(request,"hackathon.html",context) 