from django.core.management import BaseCommand
from django.db import transaction

from blog.factories import (
    PostCategoryFactory,
    PostFactory,
)


class Command(BaseCommand):
    help = 'Create factory data.'

    @transaction.atomic()
    def handle(self, *args, **options):
        PostCategoryFactory.create_batch(10)
        PostFactory.create_batch(20)
