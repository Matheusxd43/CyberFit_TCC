from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Equipamento

# Página principal que lista os equipamentos
def home(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'core/home.html', {'equipamentos': equipamentos})

# Página de detalhes do equipamento e seus vídeos/treinos
def detalhe_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    conteudos = equipamento.videos.filter(disponivel=True)
    return render(request, 'core/detalhe_equipamento.html', {
        'equipamento': equipamento,
        'conteudos': conteudos
    })
    