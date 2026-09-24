from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'equipamento/<int:pk>/',
        views.detalhe_equipamento,
        name='detalhe_equipamento'
    ),

    path(
        'avaliar/<int:conteudo_id>/',
        views.enviar_avaliacao,
        name='enviar_avaliacao'
    ),
]