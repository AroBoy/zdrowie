# from datetime import datetime
# import factory
# import random
# import factory.django
# from factory.fuzzy import FuzzyDateTime
# from pytz import UTC
#
# from zdrowie.users.tests.factories import UserFactory
#
#
#
# class BloodpressureFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = 'bloodpressures.BloodPressure'
#
#     user = factory.SubFactory(UserFactory)
#     systolic = factory.LazyAttribute(lambda x: random.randint(100, 260))
#     diastolic = factory.LazyAttribute(lambda x: random.randint(40, 120))
#
#     @factory.lazy_attribute
#     def diastolic(self):
#         diastolic = self.systolic - random.randint(20, 60)
#         return diastolic
#
#     pulse = factory.LazyAttribute(lambda x: random.randint(40, 240))
#     record_datetime = factory.LazyAttribute(lambda x: FuzzyDateTime(datetime(2021, 1, 1,tzinfo=UTC)).fuzz())
