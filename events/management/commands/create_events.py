import random
import factory
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from events.factories import CategoryFactory, EventFactory
from events.models import Category, Event

NUM_CATEGORIES = 4
NUM_EVENTS = 20

User = get_user_model()

class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):

        print("Deleting model data...")

        user_list = User.objects.all()

        for m in [Event, Category]:
            m.objects.all().delete()

        print("Creating Categories...")

        categories = []
        for _ in range(NUM_CATEGORIES):
            c = CategoryFactory()
            c.slug = slugify(c.name)
            c.save()
            categories.append(c)

        print("Creating Events...")

        # Create all the events
        for _ in range(NUM_EVENTS):
            event = EventFactory(
                category=random.choice(categories),
                author=random.choice(user_list)
            )

            event.slug = slugify(event.name)
            event.save()