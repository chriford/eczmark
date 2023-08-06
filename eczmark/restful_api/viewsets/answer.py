from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from eczmark.models import Answer
from ..serializers import AnswerSerializer

class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    def list(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        response = Response(serializer.data)
        return response
    
    def retrieve(self, request, pk):
        queryset = Answer.objects.all()
        answer_object = get_object_or_404(queryset, pk=pk)
        serializer = AnswerSerializer(answer_object)
        response = Response(serializer.data)
        return response
    
    def destroy(self, request, pk):
        queryset = Answer.objects.all()
        answer_object = get_object_or_404(queryset, pk=pk)
        if answer_object:
            answer_object.delete()
        response = Response({
            "status": "Object deleted successfully", 
            "status_code": status.HTTP_404_NOT_FOUND,
        })
        return response
