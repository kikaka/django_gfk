from rest_framework import viewsets, permissions, filters
from events import models
from .serializers import CategorySerializer, EventInlineSerializer
from rest_framework.authentication import TokenAuthentication


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name"]


class EventViewset(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = EventInlineSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name", "date"]
