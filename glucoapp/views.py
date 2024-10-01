# glucoapp/views.py

from django.contrib.auth.decorators import login_required
from django.utils.translation import activate, get_language
from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from .models import GlucoseReading
from .forms import GlucoseReadingForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm
import plotly.express as px
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    return render(request, "login.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    # Determine the current language code
    language_code = get_language()  # This gets the current language code
    # Redirect to the home page of the current language
    return redirect(f"/{language_code}/login/")  # Adjust this according to your URL structure


@login_required
def home(request):
    context = {
        'mensaje': 'Welcome to Glucose Tracker',
        'language_code': get_language(),
        # Otros contextos necesarios
    }
    return render(request, 'home.html', context)

@login_required
def add_glucose_reading(request):
    if request.method == "POST":
        form = GlucoseReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.patient = request.user
            reading.save()
            return redirect("glucose_readings")
    else:
        form = GlucoseReadingForm()
    return render(request, "add_glucose_reading.html", {"form": form})


@login_required
def glucose_readings(request):
    readings = GlucoseReading.objects.filter(patient=request.user)
    return render(request, "glucose_readings.html", {"readings": readings})

# @login_required
# def glucose_chart(request):
#     readings = GlucoseReading.objects.filter(patient=request.user)
#     df = pd.DataFrame(list(readings.values("date", "level")))
#     fig = px.line(df, x="date", y="level", title="Glucose Levels Over Time")
#     chart = fig.to_html(full_html=False)
#     return render(request, "glucose_chart.html", {"chart": chart})

# BAR CHART MODEL.
# @login_required
# def glucose_chart(request):
#     readings = GlucoseReading.objects.filter(patient=request.user)
#     df = pd.DataFrame(list(readings.values("date", "level")))
#     # Cambiar de línea a barras
#     fig = px.bar(df, x="date", y="level", title="Glucose Levels Over Time")
#     chart = fig.to_html(full_html=False)
#     return render(request, "glucose_chart.html", {"chart": chart})

# SCATTER PLOT.
# @login_required
# def glucose_chart(request):
#     readings = GlucoseReading.objects.filter(patient=request.user)
#     df = pd.DataFrame(list(readings.values("date", "level")))
#     # Cambiar a gráfico de dispersión
#     fig = px.scatter(df, x="date", y="level", title="Glucose Levels Over Time")
#     chart = fig.to_html(full_html=False)
#     return render(request, "glucose_chart.html", {"chart": chart})

# AREA CHART.
@login_required
def glucose_chart(request):
    readings = GlucoseReading.objects.filter(patient=request.user)
    df = pd.DataFrame(list(readings.values("date", "level")))
    # Cambiar a gráfico de área
    fig = px.area(df, x="date", y="level", title="Glucose Levels Over Time")
    
    fig.update_traces(line=dict(color="#007c84"))
    
    chart = fig.to_html(full_html=False)
    return render(request, "glucose_chart.html", {"chart": chart})

def change_language(request, language_code):
    next_page = request.META.get("HTTP_REFERER", "/")
    response = redirect(next_page)
    if language_code in [lang[0] for lang in settings.LANGUAGES]:
        logger.debug(f"Activating language: {language_code}")
        translation.activate(language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = language_code
        request.session.modified = True
        logger.debug(f"Language activated: {translation.get_language()}")
    else:
        logger.warning(f"Invalid language code: {language_code}")
    logger.debug(f"Redirecting to: {next_page}")
    return response


def set_language(request):
    language = request.POST.get("language")
    next_url = request.POST.get("next", "/")
    if language:
        activate(language)
    return redirect(next_url)
