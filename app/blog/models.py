from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='名前', max_length=250, unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=250, unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    slug = models.SlugField(verbose_name='URL', max_length=250, unique=True)
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー', on_delete=models.PROTECT
    )
    eyecatch = models.ImageField(
        verbose_name='サムネイル', upload_to='uploads/', max_length=320, blank=True
    )
    content = models.TextField(verbose_name='本文', max_length=50000)
    is_published = models.BooleanField(verbose_name='公開', default=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'

    def __str__(self):
        return self.title
