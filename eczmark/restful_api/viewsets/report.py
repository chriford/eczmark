from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from eczmark.models import Report
from ..serializers import ReportSerializer

class ReportViewSet(ModelViewSet):
    def list(self, request):
        queryset = Report.objects.all()
        serializer = ReportSerializer(queryset, many=True)
        response = Response(serializer.data)
        return response
    
    def retrieve(self, request, pk):
        queryset = Report.objects.all()
        report_object = get_object_or_404(queryset, pk=pk)
        serializer = ReportSerializer(report_object)
        response = Response(serializer.data)
        return response
    
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
    
