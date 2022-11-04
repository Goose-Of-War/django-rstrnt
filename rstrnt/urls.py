from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('alt', views.another_view),
	path('menu', views.show_menu),
	path('<str:item>', views.view_item, name="item")
]