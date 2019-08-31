from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'site_description')
    list_display_links = ['site_name']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'cols': 100})},
    }


admin.site.register(Setting, SettingAdmin)
