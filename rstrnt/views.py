from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from json import load, dump
from os import getcwd
# Create your views here.

class ItemForm(forms.Form):
	name = forms.CharField(label= "Name")
	price = forms.IntegerField(label= "Price", min_value= 10)
	img = forms.CharField(label= "Img link")

def index(request):
	return HttpResponse("Work in progress, please come back later ;-;")

def render_404(request):
	return render(request, '404.html', {"pagetitle": "404"})

def show_menu(request):
	try:
		with open('rstrnt/static/menu.json') as jsonfile: menu = load(jsonfile)
	except:
		with open('rstrnt/static/menu.json', 'w') as jsonfile: dump([], jsonfile)
	return render(request, "menu.html", {
		"items": menu, 
		"pagetitle": "Menu"
	})

def add_to_menu(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			try:
				with open('rstrnt/static/menu.json') as jsonfile: menu = load(jsonfile)
			except:
				with open('rstrnt/static/menu.json', 'w') as jsonfile: dump([], jsonfile)
				menu = []
			item = dict([ (i, *dict(request.POST)[i]) for i in ['name', 'price', 'img'] ])
			menu.append(item)
			with open('rstrnt/static/menu.json', 'w') as jsonfile: dump(menu, jsonfile)
			print("Reached this point ;-;")
			return HttpResponseRedirect(reverse("menu"))
		else:
			return render(request, "add_item.html", {
			"pagetitle": "Add Item",
			"form": form
		})
	else:
		return render(request, "add_item.html", {
			"pagetitle": "Add Item",
			"form": ItemForm()
		})