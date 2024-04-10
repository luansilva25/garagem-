from rest_framework.viewsets import ModelViewSet
from garagem.models import Categoria
from garagem.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == "get":
            return Categoria.objects.filter(usuario=self.request.user)
        return Categoria.objects.all()
    serializer_class = CategoriaSerializer