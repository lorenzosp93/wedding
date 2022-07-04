from rest_framework.serializers import ModelSerializer, CharField, DictField, ListField
from .models import (
    UserMessage, Response,
    User,
)
from shared.models import (
    UserProfile, Address
)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserExtendedSerializer(ModelSerializer):
    address = AddressSerializer(required=False)
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'

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
