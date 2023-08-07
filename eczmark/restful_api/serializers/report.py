
from rest_framework import serializers

from eczmark.models import Report, User, Issue
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

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        issue_data = validated_data.pop('issue', None)

        if not user_data:
            raise ValueError("Expected data for unnullable fields")
        try:
            user = User.objects.get(username = user_data.get('username'))
        except User.DoesNotExist:
            try:
                user = User.objects.get(email = user_data.get('email'))
            except User.DoesNotExist:
                raise ValueError("Expected valid user data. unique-identifiers: username, email")
                
        try:
            issue = Issue.objects.get(name=issue_data.name)
        except Issue.DoesNotExist:
            issue = Issue.objects.create(**issue_data)
        
        if not issue_data:
            raise ValueError("Expected data for unnullable fields")
        
        if not validated_data:
            raise ValueError("Expected data for unnullable fields")
        report = Report.objects.create(user=user, issue=issue, **validated_data)
        return report
    