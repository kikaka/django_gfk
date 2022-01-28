from rest_framework import viewsets
from events import models
from .serializers import CategorySerializer
from rest_framework.authentication import TokenAuthentication


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer
