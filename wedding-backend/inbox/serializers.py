from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import (
    ModelSerializer, PrimaryKeyRelatedField,
    SerializerMethodField, ValidationError
)
from .models import (
    Message, Question, Response, Option
)
from profile.serializers import (
    TranslationContentMixin, TranslationSubjectMixin,
)
from shared.serializers import HasUserSerializer


class OptionSerializer(TranslationContentMixin, ModelSerializer):

    class Meta:
        model = Option
        fields = ('uuid', 'content',)


class ResponseSerializer(HasUserSerializer):
    option = PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Option.objects.all()
    )
    question = PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Response
        fields = '__all__'

    def validate(self, data: dict) -> dict:
        question = data.get('question')
        if question and question.mandatory:
            self.validate_responses(data, question)
        return super().validate(data)

    def validate_responses(self, data: dict, question: Question) -> None:
        if question.options.count() > 0:
            if not data.get('option') and not data.get('text'):
                if question.free_text:
                    raise ValidationError({
                        "text": _(
                            "Text must be provided if no option is selected"
                        ),
                    })
                raise ValidationError({
                    'option': _("Please choose an option"),
                })
        elif not data.get('text') and question.free_text:
            raise ValidationError({
                'text': _("Text must be provided"),
            })


class QuestionSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer
):
    def get_formatted_response(self, question: Question) -> dict | None:
        request: HttpRequest | None = self.context.get('request')
        if request:
            user = request.user
            response = Response.objects.filter(
                question=question,
                user=user,
                active=True,
            ).first()
            if response:
                option_list = response.option.values_list('uuid', flat=True)
                return {
                    'option': option_list,
                    'text': response.text if response else '',
                    'uuid': response.uuid,
                }
        return None

    options = OptionSerializer(many=True, required=False)
    response = SerializerMethodField("get_formatted_response")

    class Meta:
        model = Question
        exclude = ['message']


class MessageSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer,
):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Message
        exclude = ['submit', 'modified_at', 'audience', 'option_pre',]
