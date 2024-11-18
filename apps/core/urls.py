from django.urls import path
from .views import home_view, theory_view, cards_view, sobre_nosotros_view

urlpatterns = [
    path('', home_view, name="home"),
    path('taller/', theory_view, name="theory"),
    path('tecnicas-fichaje/', cards_view, name="cards"),
    path('sobre-nosotros/', sobre_nosotros_view, name="sobre_nosotros"),
]
