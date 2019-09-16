from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostListTests(TestCase):

    def test_get(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.content['index'], [])

    # def test_post_and_get_1(self):
    