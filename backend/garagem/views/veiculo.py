from rest_framework.viewsets import ModelViewSet
from garagem.models import Veiculo
from garagem.serializers import VeiculoSerializer, VeiculoSerializerList

class VeiculoViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == 'get':
            return Veiculo.objects.filter(usuario=self.request.user)
        return Veiculo.objects.all()
    def get_serializer_class(self):
        if self.action == "create":
            return VeiculoSerializer
        return VeiculoSerializerList
   