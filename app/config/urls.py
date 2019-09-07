from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog.sitemaps import PostSitemap, StaticSitemap


admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_INDEX_TITLE


sitemaps = {
    'posts': PostSitemap,
    'static': StaticSitemap,
}


urlpatterns = [
    path('', include('blog.urls')),
    path(settings.ADMIN_URL + '/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
