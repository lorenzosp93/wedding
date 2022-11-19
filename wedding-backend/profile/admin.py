from django.contrib import admin
from .models import UserProfile, User

# Register your models here.

admin.site.unregister(User)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'type', 'plus')
    list_editable = ('language', 'type', 'plus', )
    list_filter = ('language', 'type', 'plus',)


class UserProfileInLine(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    exclude = ('parent',)
    min_num = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'profile')
    list_editable = ('first_name', 'last_name')
    inlines = [UserProfileInLine]
    fields = ('username', 'email', 'first_name', 'last_name', )
