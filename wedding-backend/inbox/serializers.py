from rest_framework.serializers import ModelSerializer, CharField, DictField, ListField
from .models import (
    UserMessage, Response,
)

class UserMessageSerializer(ModelSerializer):
    get_message_content = CharField()
    get_questions_content = DictField()
    class Meta:
        model = UserMessage
        exclude = ['message', 'id', 'user', 'isRead']

class ResponseSerializer(ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'
