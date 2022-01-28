import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    """Eine Fabrikklasse, die User generiert"""

    class Meta:
        model = get_user_model()

    email = factory.Faker("email")
    password = factory.LazyFunction(lambda: make_password('abc'))