from django.urls import path
from . import views

urlpatterns = [
	path('', views.MenuApi.as_view()),
]
