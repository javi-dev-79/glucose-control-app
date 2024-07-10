# glucoapp/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import GlucoseReading
from .forms import GlucoseReadingForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
import plotly.express as px
import pandas as pd

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'login.html', {'form': form}) 

@login_required
def home(request):
    contexto = {
        'mensaje': 'Welcome to Glucose Tracker'
    }
    return render(request, 'home.html', contexto)

@login_required
def add_glucose_reading(request):
    if request.method == 'POST':
        form = GlucoseReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.patient = request.user
            reading.save()
            return redirect('glucose_readings')
    else:
        form = GlucoseReadingForm()
    return render(request, 'add_glucose_reading.html', {'form': form})

@login_required
def glucose_readings(request):
    readings = GlucoseReading.objects.filter(patient=request.user)
    return render(request, 'glucose_readings.html', {'readings': readings})

@login_required
def glucose_chart(request):
    readings = GlucoseReading.objects.filter(patient=request.user)
    df = pd.DataFrame(list(readings.values('date', 'level')))
    fig = px.line(df, x='date', y='level', title='Glucose Levels Over Time')
    chart = fig.to_html(full_html=False)
    return render(request, 'glucose_chart.html', {'chart': chart})