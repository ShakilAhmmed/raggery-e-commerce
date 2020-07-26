from  django.urls import path
from .views import BrandApi






urlpatterns = [
    path("", BrandApi.as_view()),
    path("delete/<int:pk>", BrandApi.as_view()),
    path("status/<int:pk>", BrandApi.as_view()),
    path("<int:pk>", BrandApi.as_view()),


]