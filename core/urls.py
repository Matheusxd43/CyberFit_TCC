from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipamento//', views.detalhe_equipamento, name='detalhe_equipamento'),
]

