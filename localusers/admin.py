from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from localusers.models import LocalUser

fieldsets_new = UserAdmin.fieldsets
fieldsets_new[0][1]['fields'] += ('money',)

class LocalUserAdmin(UserAdmin):
    fieldsets = fieldsets_new

admin.site.register(LocalUser, LocalUserAdmin)
