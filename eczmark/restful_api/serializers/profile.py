
from rest_framework import serializers

from eczmark.models import Profile
from eczmark.restful_api.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = '__all__'
