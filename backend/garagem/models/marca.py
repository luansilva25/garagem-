from django.db import models
from django.contrib.auth.models import User
class Marca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False, blank=False)
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self) :
        return self.nome