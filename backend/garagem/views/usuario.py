from garagem.serializers.usuario import UserSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer