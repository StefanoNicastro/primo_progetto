from django.urls import path
from .views import *
app_name="forms_app"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('lista_contatti/', contatti, name='contatti'),
]