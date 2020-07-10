from django.urls import path
from . import views

app_name = "address"

urlpatterns = [
	path("division/", views.DivisionApi.as_view()),
	path("division/delete/<int:pk>", views.DivisionApi.as_view()),
	path("division/status/<int:pk>", views.DivisionApi.as_view()),
	path("division/<int:pk>", views.DivisionApi.as_view()),
]
