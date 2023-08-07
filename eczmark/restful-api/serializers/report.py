
from rest_framework.serializers import ModelSerializer

from eczmark.models import Report

class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
