from factory.faker import Faker as OrignFaker


class Faker(OrignFaker):
    def __init__(self, provider, **kwargs):
        return super(Faker, self).__init__(provider, locale='ja_JP', **kwargs)
