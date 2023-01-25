from django.contrib import admin
from django.utils.safestring import mark_safe, SafeString
from .models import Information, Photo, InformationWidget

# Register your models here.


class InformationWidgetInline(admin.TabularInline):
    model = InformationWidget
    extra = 1


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    def img_preview(self, obj: Photo) -> SafeString:
        return mark_safe(f'<img src = "{obj.thumbnail.url}" style="max-width:300px; max-height:300px;" />')

    list_display = ('pk', 'img_preview', 'content', 'type', 'private',)
    list_filter = ('type', 'private',)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'type', 'audience', 'content',)
    list_editable = ('subject', 'type', 'audience', 'content',)
    list_filter = ('type', 'audience',)
    inlines = [InformationWidgetInline]
