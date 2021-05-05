from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import FileResponse
from pytube import YouTube

import os

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        if request.POST['link']:
            link = request.POST['link']
            yt = YouTube(link).streams.first().download(skip_existing=True)
            print(link)
            return FileResponse(open(yt,'rb'))
        
    return render(request,'index.html')

def downloaded(request):

    return render(request,'downloaded.html')

    
    
