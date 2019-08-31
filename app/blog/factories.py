import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from common.factories import Faker
from .models import Category, Post


class PostCategoryFactory(DjangoModelFactory):
    name = FuzzyText(length=15)
    slug = FuzzyText(length=15)

    class Meta:
        model = Category


class PostFactory(DjangoModelFactory):
    title = Faker('sentence')
    description = Faker('sentence')
    slug = FuzzyText(length=15)
    category = factory.Iterator(Category.objects.all())
    eyecatch = factory.django.ImageField(
        color='red',
        height=630,
        width=1200,
    )
    content = FuzzyText(length=2000)
    is_published = True

    class Meta:
        model = Post
