from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all().order_by('-created_at')

    def location(self, obj):
        return resolve_url('blog:detail', slug=obj.slug)

    def lastmod(self, obj):
        return obj.created_at


class StaticSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['blog:index']

    def location(self, obj):
        return resolve_url(obj)
