from django.urls import path
from .views import home_view, theory_view, cards_view

urlpatterns = [
    path('', home_view, name="home"),
    path('taller/', theory_view, name="theory"),
    path('tecnicas-fichaje/', cards_view, name="cards"),
]
