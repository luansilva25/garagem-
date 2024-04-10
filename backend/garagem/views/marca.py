from garagem.models import Marca
from garagem.serializers import MarcaSerializer
from rest_framework.viewsets import ModelViewSet

class MarcaViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == "get":
            return Marca.objects.filter(usuario=self.request.user)
        return Marca.objects.all()
    serializer_class = MarcaSerializer