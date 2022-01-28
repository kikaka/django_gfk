from gc import get_debug
from wsgiref import validate
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "email", "username", "password", "date_joined"
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
            "date_joined": {"read_only": True}
        }

    def create(self, validated_data):
        """Create new user via API """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ uodate user and show user data"""
        password = validated_data.pop("password", None)

        # user mit daten hier updaten
        user = super().update(instance, validated_data)

        # falls password mitgesendet wurden, auch noch setzen
        # set_password => hash-Funktion
        if password:
            user.set_password(password)
            user.save()

        return user
