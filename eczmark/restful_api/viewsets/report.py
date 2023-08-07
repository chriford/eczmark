from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from eczmark.models import Report
from ..serializers import ReportSerializer

class ReportViewSet(ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    
    def destroy(self, request, pk):
        queryset = Report.objects.all()
        report_object = get_object_or_404(queryset, pk=pk)
        if report_object:
            report_object.delete()
        response = Response({
            "status": "Object deleted successfully", 
            "status_code": status.HTTP_404_NOT_FOUND,
        })
        return response
    
