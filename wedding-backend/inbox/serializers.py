from rest_framework.serializers import (
    ModelSerializer, CharField
)
from .models import (
    Message, Question, Response, Option
)
from profile.serializers import TranslationContentMixin


class OptionSerializer(TranslationContentMixin, ModelSerializer):
    
    class Meta:
        model = Option
        fields = '__all__'

class QuestionSerializer(TranslationContentMixin, ModelSerializer):
    options = OptionSerializer(many=True, required=False)
    type = CharField(source="get_type_display")

    class Meta:
        model = Question
        fields = '__all__'

class MessageSerializer(TranslationContentMixin, ModelSerializer):
    type = CharField(source="get_type_display")
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Message
        fields = '__all__'

class ResponseSerializer(ModelSerializer):
    option = OptionSerializer(many=True)
    class Meta:
        model = Response
        fields = '__all__'
