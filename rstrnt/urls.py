from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name= "index"),
	path('add', views.add_to_menu, name= "add_item"),
	path('menu', views.show_menu, name= "menu"),
	re_path('.*', views.render_404, name= "404")
]