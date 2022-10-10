from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    SiteSetting,
    Attachment,
    Address,
    User,
)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = [
            'uuid',
            'file'
        ]

class SettingsSerializer(ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = [
            'about_text'
        ]
