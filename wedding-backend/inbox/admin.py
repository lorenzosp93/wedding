from django.contrib import admin
from .models import Message, Question, Option, Response
# Register your models here.


class OptionInLine(admin.TabularInline):
    model = Option


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'subject', 'content', 'multi_select', 'free_text', 'mandatory'

    )
    list_editable = (
        'subject', 'content', 'multi_select', 'free_text', 'mandatory'
    )
    inlines = [
        OptionInLine,
    ]
    list_filter = ('message',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'subject', 'content', 'audience',
    )
    list_editable = (
        'subject', 'content', 'audience',
    )
    inlines = [
        QuestionInLine,
    ]
    list_filter = ('audience',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'question',
    )
    list_filter = ('user', 'question',)
