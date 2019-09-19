
import random
import string

from django.test import TestCase
from django.urls import reverse

from .factories import (
    PostCategoryFactory,
    PostFactory,
)


def get_random_name(n):
    randlst = [
        random.choice(string.ascii_letters + string.digits) for i in range(n)
    ]
    return ''.join(randlst)


class PostListTests(TestCase):

    def test_get(self):
        """getでアクセスを行う"""
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)


class PostDetailTests(TestCase):

    def test_not_found_slug_test(self):
        """存在しないslugでgetアクセス"""
        response = self.client.get(
            reverse('blog:detail', kwargs={'slug': get_random_name(10)})
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """getで通常のアクセスを行う"""
        category = PostCategoryFactory()
        post = PostFactory(category=category, eyecatch=None)
        response = self.client.get(
            reverse('blog:detail', kwargs={'slug': post.slug}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.content)


class PostListByCategoryTests(TestCase):

    def test_not_found_slug_test(self):
        """存在しないslugでgetアクセス"""
        response = self.client.get(
            reverse('blog:category', kwargs={'slug': get_random_name(10)})
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """getでアクセスを行う"""
        category = PostCategoryFactory()
        response = self.client.get(
            reverse('blog:category', kwargs={'slug': category.slug}),
        )
        self.assertEqual(response.status_code, 200)
