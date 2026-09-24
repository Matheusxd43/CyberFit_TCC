from django.contrib import admin
from django.db.models import Avg
from .models import Equipamento, ConteudoDigital, AvaliacaoUsuario


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome", "descricao")


@admin.register(ConteudoDigital)
class ConteudoDigitalAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "equipamento",
        "disponivel",
    )

    list_filter = (
        "disponivel",
        "equipamento",
    )

    search_fields = (
        "titulo",
        "descricao",
        "equipamento__nome",
    )

    list_editable = (
        "disponivel",
    )


@admin.register(AvaliacaoUsuario)
class AvaliacaoUsuarioAdmin(admin.ModelAdmin):

    change_list_template = "admin/avaliacoes_change_list.html"

    list_display = (
        "conteudo",
        "equipamento",
        "nota_visual",
        "comentario",
        "data_hora",
    )

    list_filter = (
        "nota",
        "conteudo__equipamento",
        "data_hora",
    )

    search_fields = (
        "conteudo__titulo",
        "conteudo__equipamento__nome",
        "comentario_texto",
    )

    readonly_fields = (
        "data_hora",
    )

    ordering = (
        "-data_hora",
    )

    # Calcula a média e o total de avaliações
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        avaliacoes = AvaliacaoUsuario.objects.all()

        total = avaliacoes.count()
        media = avaliacoes.aggregate(
            media=Avg("nota")
        )["media"]

        extra_context["total_avaliacoes"] = total
        extra_context["media_avaliacoes"] = (
            round(media, 1) if media else 0
        )

        return super().changelist_view(
            request,
            extra_context=extra_context
        )

    # Impede avaliações manuais pelo administrador
    def has_add_permission(self, request):
        return False

    # Equipamento relacionado ao conteúdo
    @admin.display(description="Equipamento")
    def equipamento(self, obj):
        return obj.conteudo.equipamento.nome

    # Nota em estrelas
    @admin.display(description="Nota", ordering="nota")
    def nota_visual(self, obj):
        estrelas_cheias = "★" * obj.nota
        estrelas_vazias = "☆" * (5 - obj.nota)

        return f"{estrelas_cheias}{estrelas_vazias} {obj.nota}/5"

    # Comentário
    @admin.display(description="Comentário")
    def comentario(self, obj):
        if not obj.comentario_texto:
            return "Sem comentário"

        if len(obj.comentario_texto) > 80:
            return obj.comentario_texto[:80] + "..."

        return obj.comentario_texto