from django.urls import path
from . import views

app_name = "menu"
urlpatterns = [
	path("", views.MenuApi.as_view()),
	path("delete/<int:pk>", views.MenuApi.as_view()),
	path("status/<int:pk>", views.MenuApi.as_view()),
	path("<int:pk>", views.MenuApi.as_view()),
]
