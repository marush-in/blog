from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at')
    list_editable = ['name', 'slug']
    list_per_page = 20


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 6, 'cols': 100})},
    }
    list_display = (
        'id', 'title', 'slug', 'is_published', 'post_eyecatch', 'created_at',
    )
    list_display_links = ['title']
    list_editable = ['is_published']
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
