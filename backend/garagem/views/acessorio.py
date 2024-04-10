from rest_framework.viewsets import ModelViewSet
from garagem.models import Acessorio
from garagem.serializers import AcessorioSerializer

class AcessorioViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == "get":
            return Acessorio.objects.filter(usuario=self.request.user)
        return Acessorio.objects.all()
    serializer_class = AcessorioSerializer