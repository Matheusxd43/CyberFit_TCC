from django.db import models
from django.contrib.auth.models import User


class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class ConteudoDigital(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, related_name="videos"
    )
    link_video = models.URLField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class AvaliacaoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(
        ConteudoDigital, on_delete=models.CASCADE, related_name="avaliacoes"
    )
    nota = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )  # Escala de 1 a 5
    comentario_texto = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota {self.nota} para {self.conteudo.titulo}"
