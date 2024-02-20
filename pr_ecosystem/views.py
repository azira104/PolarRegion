from django.shortcuts import render

# Create your views here.
def freshwater(request):
    return render(request, 'freshwater.html')

def marine(request):
    return render(request, 'marine.html')

def terrestrial(request):
    return render(request, 'terrestrial.html')