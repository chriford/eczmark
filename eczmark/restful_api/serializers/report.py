
from rest_framework import serializers

from eczmark.models import Report
from .user import UserSerializer
from .issue import IssueSerializer

class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    issue = IssueSerializer()
    class Meta:
        model = Report
        fields = [
            'user',
            'issue',
            'message',
            'active',
        ]
