from django.contrib import admin
from .models import SiteSetting, Attachment, UserProfile

# Register your models here.
admin.site.register(SiteSetting)
admin.site.register(Attachment)
admin.site.register(UserProfile)
