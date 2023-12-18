from django.shortcuts import render

# Create your views here.
def penguinpopu(request):
    return render(request, 'penguinpopu.html')

def palmer(request):
    return render(request, 'palmer.html')

def mfungi(request):
    return render(request, 'mfungi.html')