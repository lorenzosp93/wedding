from rest_framework.serializers import (
    ModelSerializer, CharField, PrimaryKeyRelatedField, 
)
from .models import (
    Message, Question, Response, Option, User
)
from profile.serializers import TranslationContentMixin, TranslationSubjectMixin


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

class MessageSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer,
):
    type = CharField(source="get_type_display")
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Message
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

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        user_id = self.context.get('user_id')
        kwargs["user"] = User.objects.get(id=user_id)
        return super().save(**kwargs)

