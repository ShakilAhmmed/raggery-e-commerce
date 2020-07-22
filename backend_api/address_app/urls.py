from django.urls import path
from . import views, district_views

app_name = "address"

urlpatterns = [
	path("division/", views.DivisionApi.as_view()),
	path("all_division/", views.GetAllDivisionApi.as_view()),
	path("division/delete/<int:pk>", views.DivisionApi.as_view()),
	path("division/status/<int:pk>", views.DivisionApi.as_view()),
	path("division/<int:pk>", views.DivisionApi.as_view()),

	# district

	path("district/", district_views.DistrictApi.as_view()),
	path("all_district/", district_views.GetAllDistrictApi.as_view()),
	path("district/delete/<int:pk>", district_views.DistrictApi.as_view()),
	path("district/status/<int:pk>", district_views.DistrictApi.as_view()),
	path("district/<int:pk>", district_views.DistrictApi.as_view()),
]
