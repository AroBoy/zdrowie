# from datetime import datetime
# import factory
# import random
# import factory.django
# from factory.fuzzy import FuzzyDateTime
# from pytz import UTC
# from zdrowie.users.tests.factories import UserFactory
#
# class GlucoseFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = "glucoses.Glucose"
#
#     user = factory.SubFactory(UserFactory)
#     value = factory.LazyAttribute(lambda x: random.randint(60, 350))
#     record_datetime = factory.LazyAttribute(lambda x: FuzzyDateTime(datetime(2021, 1, 1, tzinfo=UTC)).fuzz())
