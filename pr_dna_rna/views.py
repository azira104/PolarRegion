from django.shortcuts import render

# Create your views here.
def bacteria(request):
    return render(request, 'bacteria.html')

def iceKrill(request):
    return render(request, 'iceKrill.html')

def phytoplankton(request):
    return render(request, 'phytoplankton.html')

def plankton(request):
    return render(request, 'plankton.html')