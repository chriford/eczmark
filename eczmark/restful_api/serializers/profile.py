
from rest_framework import serializers

from eczmark.models import Profile, User
from eczmark.restful_api.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)

        if not user_data:
            raise ValueError("Expected data for unnullable fields")
        user = User.objects.create(**user_data)

        profile = Profile.objects.create(user=user, **validated_data)
        return profile
