from django.db import models

class Cor(models.Model):
    descricao = models.CharField(max_length=25)

    def __str__(self):
        return self.descricao