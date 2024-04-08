from django.db import models
from garagem import models as itens
from uploader.models.image import Image
from django.contrib.auth.models import User

class Veiculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    foto = models.ForeignKey(Image, related_name='+', on_delete=models.PROTECT,default=None, blank=True, null=True)
    nome = models.CharField(max_length=100, default=None)
    marca = models.ForeignKey(itens.Marca, on_delete=models.PROTECT, related_name="marca")
    categoria = models.ForeignKey(itens.Categoria, on_delete=models.PROTECT, related_name="categoria")
    cor = models.ForeignKey(itens.Cor, on_delete=models.PROTECT,related_name="cor")
    acessorio = models.ManyToManyField(itens.Acessorio)
    ano = models.IntegerField(default=0,null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} - {self.ano} - {self.categoria} - {self.cor}"
