from django.urls import path

from .views import index, previsao, CreateCity

urlpatterns = [
    path("", index, name="weather_index"),
    path("previsao/<int:pk>", previsao, name="previsao"),
    path("cidade/nova", CreateCity.as_view(), name="create_city"),
]
