from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()  # <- exactly serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # <- literally this string
            username=validated_data['username'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # <- literally this string
        return user
