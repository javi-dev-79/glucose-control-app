from django.shortcuts import render

def index(request):
    contexto = {
        'mensaje': 'Hola Mundo!'
    }
    return render(request, 'index.html', contexto)