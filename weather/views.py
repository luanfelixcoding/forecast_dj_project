from django.shortcuts import render
from weather.models import City


def index(request):
    cities = City.objects.all()
    return render(request, "weather/index.html", {"cities": cities})
