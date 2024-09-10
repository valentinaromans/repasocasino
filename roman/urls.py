from django.urls import path
from . import views

urlpatterns = [
    path('', views.sepulveda),
    path('danitza/', views.danitza),
]