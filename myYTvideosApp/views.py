from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import FileResponse
from pytube import YouTube

import os
import time

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        if request.POST['link']:
            link = request.POST['link']
            yt = YouTube(link).streams.first().download(skip_existing=True)
            print(link)
<<<<<<< HEAD
            time.sleep(10)
            return redirect('/downloaded')
=======
            return FileResponse(open(yt,'rb'))
>>>>>>> f3f9ca3b2795efee67bd7b71732cd83fce1e5511
        
    return render(request,'index.html')

def downloaded(request):

    return render(request,'downloaded.html')

    
    
