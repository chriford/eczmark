
from rest_framework import serializers

from eczmark.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'created_at',
            'updated_at',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'date',
        ]
