from django.urls import path
from .views import ColorApi 


from django.urls import path

urlpatterns = [
    path("", ColorApi.as_view()),
    path("delete/<int:pk>", ColorApi.as_view()),
    path("status/<int:pk>", ColorApi.as_view()),
    path("<int:pk>", ColorApi.as_view()),


]
