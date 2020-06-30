from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from localusers.models import LocalUser

admin.site.register(LocalUser, UserAdmin)
