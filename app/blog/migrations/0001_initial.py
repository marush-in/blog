# Generated by Django 2.2.3 on 2019-08-10 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='名前')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'カテゴリー',
                'verbose_name_plural': 'カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='タイトル')),
                ('description', models.TextField(max_length=240, verbose_name='ディスクリプション')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('eyecatch', models.ImageField(blank=True, max_length=320, upload_to='uploads/', verbose_name='サムネイル')),
                ('content', models.TextField(max_length=50000, verbose_name='本文')),
                ('is_published', models.BooleanField(default=False, verbose_name='公開')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリー')),
            ],
            options={
                'verbose_name': '記事',
                'verbose_name_plural': '記事',
            },
        ),
    ]