from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, min_length=8)

    def create(self, validated_data):
        # Use create_user to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Create an auth token for the new user
        Token.objects.create(user=user)
        return user
