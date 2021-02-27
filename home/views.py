from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')

def appointment(request):
    return render(request, 'home/appointment.html')