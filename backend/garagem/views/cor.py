from rest_framework.viewsets import ModelViewSet
from garagem.serializers import CorSerializer
from garagem.models import Cor

class CorViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == "get":
            return Cor.objects.filter(usuario=self.request.user)
        return Cor.objects.all()
    serializer_class = CorSerializer