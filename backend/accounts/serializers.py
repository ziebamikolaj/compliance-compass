from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'phone', 'address', 'date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser']
        read_only_fields = ['date_joined', 'last_login', 'id', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        