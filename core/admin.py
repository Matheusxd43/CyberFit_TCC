from django.contrib import admin
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
    list_display = (
        "usuario",
        "conteudo",
        "nota",
        "data_hora",
    )

    list_filter = (
        "nota",
        "data_hora",
    )

    search_fields = (
        "usuario__username",
        "conteudo__titulo",
        "comentario_texto",
    )

    readonly_fields = (
        "data_hora",
    )