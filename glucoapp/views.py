from django.shortcuts import render

def index(request):
    contexto = {
        'mensaje': 'Gluco Control App'
    }
    return render(request, 'index.html', contexto)

def uno(request):
    contexto = {
        'mensaje': 'Página Uno'
    }
    return render(request, 'uno.html', contexto)

def dos(request):
    contexto = {
        'mensaje': 'Página Dos'
    }
    return render(request, 'dos.html', contexto)

def tres(request):
    contexto = {
        'mensaje': 'Página Tres'
    }
    return render(request, 'tres.html', contexto)