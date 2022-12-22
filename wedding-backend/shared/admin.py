from django.contrib import admin
from .models import ContentString, TranslatedString, Address

# Register your models here.
admin.site.register(Address)


class TranslatedStringInline(admin.TabularInline):
    model = TranslatedString
    extra = 2
    max_num = 2


@admin.register(ContentString)
class ContentStringAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', )
    list_editable = ('value', )
    inlines = [
        TranslatedStringInline,
    ]


@admin.register(TranslatedString)
class TranslatedStringAdmin(admin.ModelAdmin):
    list_display = ('id', 't9n', 'content', 'language',)
    list_editable = ('t9n', 'language', 'content',)
    list_display_links = ('id',)
    list_filter = ('language',)
