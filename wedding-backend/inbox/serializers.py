from rest_framework.serializers import (
    ModelSerializer, CharField, PrimaryKeyRelatedField,
    SerializerMethodField, ValidationError
)
from .models import (
    Message, Question, Response, Option
)
from profile.serializers import TranslationContentMixin, TranslationSubjectMixin

class OptionSerializer(TranslationContentMixin, ModelSerializer):
    
    class Meta:
        model = Option
        fields = '__all__'

class ResponseSerializer(ModelSerializer):
    option = PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Option.objects.all()
    )
    question = PrimaryKeyRelatedField(queryset=Question.objects.all())
    user = PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Response
        fields = '__all__'

    def validate(self, data):
        if (len(data.get('option')) == 0 and not data.get('text')):
            raise ValidationError({
                "text": "Text must be provided if no option is selected."
            })
        return super().validate(data)

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.context.get('request').user
        return super().save(**kwargs)

class QuestionSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer
):
    def get_response(self, obj):
        user = self.context.get('request').user
        response = Response.objects.filter(question=obj, user=user).first()
        if response:
            option_list = response.option.values_list('uuid', flat=True)
            return {
                'option': option_list[0] if len(option_list) == 1  and not response.question.multi_select else option_list,
                'text': response.text if response else '',
                'uuid': response.uuid,
            }
        return None

    options = OptionSerializer(many=True, required=False)
    response = SerializerMethodField("get_response") 

    class Meta:
        model = Question
        fields = '__all__'

class MessageSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer,
):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Message
        fields = '__all__'
