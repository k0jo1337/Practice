from django.shortcuts import render

def entrance(request):
    return render(request, 'entrance/entrance.html')

def registration(request):
    return render(request, 'registration/registration.html')