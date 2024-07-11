# # glucoapp/urls.py

# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("", views.home, name="home"),
#     path("login/", views.login_view, name="login"),
#     path("logout/", views.logout_view, name="logout"),
#     path("readings/", views.glucose_readings, name="glucose_readings"),
#     path("add/", views.add_glucose_reading, name="add_glucose_reading"),
#     path("chart/", views.glucose_chart, name="glucose_chart"),
#     path('change-language/<str:language_code>/', views.change_language, name='change_language'),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("readings/", views.glucose_readings, name="glucose_readings"),
    path("add/", views.add_glucose_reading, name="add_glucose_reading"),
    path("chart/", views.glucose_chart, name="glucose_chart"),
    path('change-language/<str:language_code>/', views.change_language, name='change_language'),
]

# Añadir soporte para archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

