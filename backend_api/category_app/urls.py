from django.urls import path
from . import views

app_name = "category"
urlpatterns = [
	path("", views.CategoryApi.as_view()),
	path("all_category", views.GetCategoryApi.as_view()),
	path("menu_wise_category/<int:menu>", views.MenuWiseCategoryApi.as_view()),
	path("delete/<int:pk>", views.CategoryApi.as_view()),
	path("status/<int:pk>", views.CategoryApi.as_view()),
	path("<int:pk>", views.CategoryApi.as_view()),
]
