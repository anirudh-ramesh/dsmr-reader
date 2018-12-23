from django.contrib.auth.models import Group, User
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from dsmr_backend.models.settings import BackendSettings


# There is no global admin.py, so we'll just disable Group & User here.
admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(BackendSettings)
class BackendSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        (
            None, {
                'fields': ['language'],
            }
        ),
    )
