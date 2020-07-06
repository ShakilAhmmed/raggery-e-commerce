from django.urls import path
from . import views

app_name = "subcategory"
urlpatterns = [
	path("", views.SubCategoryApi.as_view()),
	path("delete/<int:pk>", views.SubCategoryApi.as_view()),
	path("status/<int:pk>", views.SubCategoryApi.as_view()),
	path("<int:pk>", views.SubCategoryApi.as_view()),
]
