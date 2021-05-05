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
            print(link)
            time.sleep(5)
            return FileResponse(open(YouTube(link).streams.first().download(skip_existing=True),'rb'))
        
    return render(request,'index.html')

def downloaded(request):

    return render(request,'downloaded.html')

    
    
