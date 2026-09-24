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
        Equipamento,
        on_delete=models.CASCADE,
        related_name="videos"
    )

    link_video = models.URLField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    def get_embed_url(self):
        """Converte diferentes formatos de URL do YouTube para embed."""

        url = self.link_video

        if not url:
            return ""

        # Link curto
        if "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1]
            video_id = video_id.split("?")[0]
            video_id = video_id.split("&")[0]

            return f"https://www.youtube.com/embed/{video_id}"

        # Link tradicional
        if "watch?v=" in url:
            video_id = url.split("watch?v=")[1]
            video_id = video_id.split("&")[0]

            return f"https://www.youtube.com/embed/{video_id}"

        # YouTube Shorts
        if "/shorts/" in url:
            video_id = url.split("/shorts/")[1]
            video_id = video_id.split("?")[0]

            return f"https://www.youtube.com/embed/{video_id}"

        # YouTube Live
        if "/live/" in url:
            video_id = url.split("/live/")[1]
            video_id = video_id.split("?")[0]

            return f"https://www.youtube.com/embed/{video_id}"

        # Link que já está no formato embed
        if "/embed/" in url:
            return url

        return ""


class AvaliacaoUsuario(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    conteudo = models.ForeignKey(
        ConteudoDigital,
        on_delete=models.CASCADE,
        related_name="avaliacoes"
    )

    nota = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )

    comentario_texto = models.TextField(
        blank=True
    )

    data_hora = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Nota {self.nota} para {self.conteudo.titulo}"