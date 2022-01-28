import arrow
from rest_framework import serializers
from events import models


class EventInlineSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    days_to_event = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = "author", "name", "date", "sub_title", "days_to_event"

    def get_days_to_event(slef, object):
        diff = object.date - arrow.now()
        return diff.days


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        # fields = "__all__"
        exclude = "slug",

    events = EventInlineSerializer(many=True, read_only=True)
