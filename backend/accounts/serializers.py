from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'phone', 'address', 'date_joined',
                  'last_login', 'is_active', 'is_admin', 'is_staff',
                  'is_superuser')
        read_only_fields = ('id', 'date_joined', 'last_login', 'is_active',
                            'is_admin', 'is_staff', 'is_superuser')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(validated_data['email'],
                                           validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
