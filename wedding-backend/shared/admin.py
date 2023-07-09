import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import ContentString, TranslatedString

# Register your models here.

CSV_ADDITIONAL_SEPARATOR = '|'


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta

        field_names = [
            field.name for field in meta.get_fields()
        ]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = []
            for field in field_names:
                if hasattr(obj, field):
                    row.append(getattr(obj, field))
                else:
                    row.append("")
            for idx, el in enumerate(row):
                if hasattr(el, 'all'):
                    row[idx] = CSV_ADDITIONAL_SEPARATOR.join(
                        str(e)
                        for e in el.all()
                    )
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Export selected %(verbose_name_plural)s"


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
