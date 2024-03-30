from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ['email', 'name']}),
        (
            _('Permissions'),
            {
                'fields': [
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ]
            }
        ),
        (_('Important Dates'), {'fields': ['last_login',]}),
    )
    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)
