from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    SiteSetting,
    Attachment
)

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
