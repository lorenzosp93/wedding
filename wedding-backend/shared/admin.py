from django.contrib import admin
from .models import SiteSettings, Attachment, UserProfile

# Register your models here.
admin.site.register(SiteSettings)
admin.site.register(Attachment)
admin.site.register(UserProfile)
