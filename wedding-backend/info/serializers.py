from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    Information, Photo
)

class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
