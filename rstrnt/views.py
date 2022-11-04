from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return HttpResponse("Work in progress, please come back later ;-;")

def another_view(request):
	return HttpResponse("You shouldn't be seeing this one... Go back ;-;")