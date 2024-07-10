# glucoapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Esta es la URL para la vista 'home'
    path('login/', views.login_view, name='login'),
    path('readings/', views.glucose_readings, name='glucose_readings'),
    path("add/", views.add_glucose_reading, name="add_glucose_reading"),
    path("chart/", views.glucose_chart, name="glucose_chart"),
]