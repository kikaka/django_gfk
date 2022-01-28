from django.core.exceptions import ValidationError
from django.utils import timezone


def datetime_future(instance_datetime):
    if instance_datetime <= timezone.now():
        raise ValidationError(
            "Der Zeitpunkt des Events muss in der Zukunft liegen!"
        )
