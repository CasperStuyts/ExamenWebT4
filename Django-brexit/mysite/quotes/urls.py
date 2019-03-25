from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
	path('', views.index, name='index'),
	
	path('<str:author_name>/', views.detail, name='detail'),
]
