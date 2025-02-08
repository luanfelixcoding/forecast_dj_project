from django.urls import path

from .views import index, previsao

urlpatterns = [
    path("", index, name="weather_index"),
    path("previsao/<int:pk>", previsao, name="previsao"),
]
