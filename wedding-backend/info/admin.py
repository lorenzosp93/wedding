import base64
from django import forms
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import URLPattern, path
from django.utils.safestring import mark_safe, SafeString
from wedding.tasks import process_photos_task
from .models import Information, Photo, InformationWidget

# Register your models here.


class InformationWidgetInline(admin.TabularInline):
    model = InformationWidget
    extra = 1

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadPhotosForm(forms.Form):
    type = forms.ChoiceField(choices=Photo.type.field.choices, required=True)
    photos = MultipleImageField()


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    change_list_template = "info/photo_admin.html"
    def img_preview(self, obj: Photo) -> SafeString:
        return mark_safe(f'<img src = "{obj.thumbnail.url}" style="max-width:300px; max-height:300px;" />')

    
    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        my_urls = [
            path(
                'upload-photos/', self.upload_photos,
                name='upload-photos'
            ),
        ]
        return my_urls + urls

    def upload_photos(self, request: HttpRequest) -> HttpResponse:
        # This function will handle the bulk upload of photos
        if request.method == 'POST':
            form = UploadPhotosForm(request.POST, request.FILES)
            if form.is_valid():
                type = form.cleaned_data.get('type')
                photos = form.cleaned_data.get('photos')
                for photo in photos:
                    encoded_photo = base64.b64encode(photo.read()).decode('utf8')
                    filename = photo.name
                    process_photos_task.delay(
                        type,
                        encoded_photo,
                        filename,
                    )
                message, level = "Your photos upload will be processed soon", "SUCCESS"
                self.message_user(
                    request, message, level
                )
                return redirect("..")
            self.message_user(
                request, form.errors.as_text(), level='ERROR'
            )
            return redirect("..")
        form = UploadPhotosForm()
        payload = {"form": form}
        return render(
            request, "custom_form.html", payload
        )

    list_display = ('pk', 'img_preview', 'content', 'type', 'private',)
    list_filter = ('type', 'private',)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'type', 'audience', 'content',)
    list_editable = ('subject', 'type', 'audience', 'content',)
    list_filter = ('type', 'audience',)
    inlines = [InformationWidgetInline]
