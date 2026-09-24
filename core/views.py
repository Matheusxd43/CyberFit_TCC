from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Equipamento, ConteudoDigital, AvaliacaoUsuario


# Página principal que lista os equipamentos
def home(request):
    equipamentos = Equipamento.objects.all()

    return render(
        request,
        'core/home.html',
        {'equipamentos': equipamentos}
    )


# Página de detalhes do equipamento e seus vídeos/treinos
def detalhe_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)

    conteudos = equipamento.videos.filter(disponivel=True)

    return render(
        request,
        'core/detalhe_equipamento.html',
        {
            'equipamento': equipamento,
            'conteudos': conteudos
        }
    )


# Recebe e salva a avaliação enviada pelo usuário
def enviar_avaliacao(request, conteudo_id):

    if request.method == 'POST':

        conteudo = get_object_or_404(
            ConteudoDigital,
            pk=conteudo_id
        )

        nota = request.POST.get('nota')
        comentario = request.POST.get(
            'comentario',
            ''
        ).strip()

        if nota:

            AvaliacaoUsuario.objects.create(
                usuario=(
                    request.user
                    if request.user.is_authenticated
                    else None
                ),
                conteudo=conteudo,
                nota=int(nota),
                comentario_texto=comentario
            )

            messages.success(
                request,
                'Obrigado! Sua avaliação foi enviada com sucesso.'
            )

        return redirect(
            'detalhe_equipamento',
            pk=conteudo.equipamento.pk
        )

    return redirect('home')