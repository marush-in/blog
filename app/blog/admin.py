from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Post, PostAdmin)
