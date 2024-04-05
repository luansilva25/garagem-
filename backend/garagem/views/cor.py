from rest_framework.viewsets import ModelViewSet
from garagem.serializers import CorSerializer
from garagem.models import Cor

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer