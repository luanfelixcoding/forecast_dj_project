from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

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


class CreateCity(CreateView):
    model = City
    fields = ["name", "state", "country", "lat", "long"]
    template_name = "weather/cidade_form.html"
    success_url = reverse_lazy("weather_index")
