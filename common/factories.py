import factory

class UserFactory(factory.django.DjangoModelFactory):


    class Meta:
        model = "users.User"
        django_get_or_create = ('email',)


    email = factory.Sequence(lambda n: f'user-{n}@pywww.pl')
    username = factory.Sequence(lambda n: f'user{n}')
    password = "123"
