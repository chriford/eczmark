
from rest_framework.serializers import ModelSerializer

from eczmark.models import Issue

class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
