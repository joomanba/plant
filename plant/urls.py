from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_main, name='plant_main'),
    path('list', views.plant_list, name='plant_list'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('search', views.plant_search, name='plant_search'),
]
