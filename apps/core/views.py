from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")


def theory_view(request):
    return render(request, "theory.html")


def cards_view(request):
    return render(request, "cards.html")

