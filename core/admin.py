from django.contrib import admin
from .models import Equipamento, ConteudoDigital, AvaliacaoUsuario

# Registrando os modelos do CyberFit no painel do administrador
admin.site.register(Equipamento)
admin.site.register(ConteudoDigital)
admin.site.register(AvaliacaoUsuario)
