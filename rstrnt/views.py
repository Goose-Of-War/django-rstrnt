from django.http import HttpResponse
from django.shortcuts import render
from json import load
from os import getcwd
# Create your views here.

def index(request):
	return HttpResponse("Work in progress, please come back later ;-;")

def another_view(request):
	return HttpResponse("You shouldn't be seeing this one... Go back ;-;")

def view_item(request, item: str):
	#return HttpResponse(f"One order of {item.lower()} coming right up? No wait. We ain't up yet ;-;")
	return render(request, "item_template.html", {'item': item.lower()})

def show_menu(request):
	with open('rstrnt\\static\\menu.json') as jsonfile: menu = load(jsonfile)
	return render(request, "menu.html", {"items": menu})