from django.shortcuts import render


def index(request) -> render:
    return render(request, "projeto/home.html")
