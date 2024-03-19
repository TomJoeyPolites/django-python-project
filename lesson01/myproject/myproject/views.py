# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  # return HttpResponse("Hey Fam, I'm Home.")
  return render(request, 'home.html')

def about(request):
  # return HttpResponse("About Me!")
  return render(request, 'about.html')