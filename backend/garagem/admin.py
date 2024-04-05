from django.contrib import admin
from .models import Marca, Categoria, Veiculo, Cor, Acessorio

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', )

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ("descricao", )

@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    list_display = ("descricao", )

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("marca", "preco", "ano")
    
