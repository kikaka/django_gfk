from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from user.factories import UserFactory

User = get_user_model()
usernames = [
    "Bob",
    "Alice",
    "Carol",
    "Mallory",
    "Eve",
    "Oscar",
    "Victor",
    "Trudy",
    "Trend"
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Delete Users ...")
        User.objects.exclude(username="admin").delete()
        for username in usernames:
            UserFactory(username=username)
            
