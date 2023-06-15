from django.contrib import admin
from .models import Message, Question, Option, Response
from shared.admin import ExportCsvMixin
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
class ResponseAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        'user', 'question', 'get_options', 'text', 'active', 'deleted_at'
    )
    list_filter = ('user', 'question', 'active')
    actions = ['export_as_csv']
