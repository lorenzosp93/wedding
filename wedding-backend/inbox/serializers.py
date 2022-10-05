from rest_framework.serializers import ModelSerializer, CharField, DictField, BooleanField
from .models import (
    UserMessage, Response, Option
)

class UserMessageSerializer(ModelSerializer):
    get_message_content = CharField()
    get_questions_content = DictField()
    class Meta:
        model = UserMessage
        exclude = ['message', 'id', 'user',]

class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class ResponseSerializer(ModelSerializer):
    option = OptionSerializer(many=True)
    class Meta:
        model = Response
        fields = '__all__'
