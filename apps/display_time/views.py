from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
import datetime

def index(request):
    now = datetime.datetime.now()
    
    now = now.strftime("%b %d %Y %I:%M %p")
    time = {
        "time": now
    }
    return render(request, "display_time/index.html",time)
