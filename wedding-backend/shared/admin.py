from django.contrib import admin
from .models import SiteSetting, Attachment, ContentString, TranslatedString, Address

# Register your models here.
admin.site.register(SiteSetting)
admin.site.register(Address)
admin.site.register(Attachment)
admin.site.register(ContentString)
admin.site.register(TranslatedString)
