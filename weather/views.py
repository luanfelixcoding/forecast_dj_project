from django.shortcuts import render, get_object_or_404
from weather.models import City
from weather.utils import get_weather


def index(request):
    cities = City.objects.all()
    return render(request, "weather/index.html", {"cities": cities})


def previsao(request, pk: int):
    city = get_object_or_404(City, pk=pk)
    prev = get_weather(city.lat, city.long)
    return render(request,
                  "weather/previsao.html",
                  {
                      "city": city,
                      "prevision": prev,
                  }
                  )
