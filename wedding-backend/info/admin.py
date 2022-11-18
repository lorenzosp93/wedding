from django.contrib import admin
from .models import Information, Photo

# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'picture', 'private',)
    list_filter = ('type', 'private',)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'type', 'audience', 'content',)
    list_editable = ('subject', 'type', 'audience', 'content',)
    list_filter = ('type', 'audience',)
