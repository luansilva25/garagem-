from django.db import models
from django.contrib.auth.models import User
class Acessorio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False, blank=False)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao