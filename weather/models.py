from django.db import models


class City(models.Model):
    name: str = models.CharField(max_length=255)
    state: str = models.CharField(max_length=255)
    country: str = models.CharField(max_length=255)
    lat: float = models.FloatField()
    long: float = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.state} - {self.country}"


class Prevision(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    time_max: float = models.FloatField()
    time_min: float = models.FloatField()
