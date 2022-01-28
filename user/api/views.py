from django.contrib.auth import get_user_model
from user.forms import User
from .serializers import UserSerializer
from rest_framework import generics, authentication, permissions


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserManageView(generics.RetrieveUpdateAPIView):
    """ manage authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = authentication.TokenAuthentication,
    permission_classes = permissions.IsAuthenticated,

    def get_object(self):
        """ das ist für die Detailansicht"""
        return self.request.user
