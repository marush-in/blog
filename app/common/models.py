from django.db import models


class Setting(models.Model):
    site_name = models.CharField(verbose_name='サイト名', max_length=160)
    site_description = models.TextField(verbose_name='サイトの説明', max_length=240)
    ogp_image = models.ImageField(
        verbose_name='OGP画像', upload_to='uploads/', max_length=320, blank=True
    )
    profile_icon = models.ImageField(
        verbose_name='プロフィール画像',
        upload_to='uploads/',
        max_length=320,
        blank=True
    )
    profile_info = models.TextField(verbose_name='プロフィール情報', max_length=240)
    ga_tag = models.TextField(
        verbose_name='GoogleAnalyticsタグ', max_length=600, blank=True
    )
    email = models.CharField(
        verbose_name='メールアドレス', max_length=240, blank=True
    )
    twitter = models.CharField(
        verbose_name='Twitter', max_length=240, blank=True
    )
    github = models.CharField(
        verbose_name='GitHub', max_length=240, blank=True
    )
    is_public = models.BooleanField(
        verbose_name='検索エンジンに登録する', default=True
    )
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'サイト基本情報'
        verbose_name_plural = 'サイト基本情報'

    def __str__(self):
        return self.site_name
