from django.contrib import admin

from .models import Category, Post


admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)
