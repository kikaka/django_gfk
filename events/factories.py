import arrow
import factory
from django.utils import timezone
from django.contrib.auth import get_user_model
from .import models

User = get_user_model()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Iterator(["Sport", "Talk", "Kochen", "Freizeit"])
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph")


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event

    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    min_group = factory.Iterator([1, 5, 10, 20])
    description = factory.Faker('paragraph')

    date = factory.Faker(
        "date_time_between",
        end_date=arrow.utcnow().shift(days=+60).datetime,
        start_date=arrow.utcnow().datetime,
        tzinfo=timezone.get_current_timezone(),
    )