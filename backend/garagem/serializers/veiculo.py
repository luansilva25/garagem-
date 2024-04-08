from rest_framework.serializers import ModelSerializer, SlugRelatedField
from garagem.models import Veiculo
from uploader.models.image import Image
from uploader.serializers import ImageSerializer
class VeiculoSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset = Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True
    )
    foto = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Veiculo
        fields = '__all__'

class VeiculoSerializerList(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset = Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True
    )
    foto = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Veiculo
        fields = '__all__'
        depth = 1