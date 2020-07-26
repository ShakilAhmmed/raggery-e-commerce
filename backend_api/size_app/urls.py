from  django.urls import path
from .views import SizeApi






urlpatterns = [
    path("", SizeApi.as_view()),
    path("delete/<int:pk>", SizeApi.as_view()),
    path("status/<int:pk>", SizeApi.as_view()),
    path("<int:pk>", SizeApi.as_view()),


]