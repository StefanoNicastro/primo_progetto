from django.urls import path
from .views import *
app_name='news'

urlpatterns = [
    path('', home, name="homeview"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("query_base", query_base,name="query_base")
]