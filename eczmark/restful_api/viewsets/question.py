from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from eczmark.models import Question
from ..serializers import QuestionSerializer

class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def destroy(self, request, pk):
        queryset = Question.objects.all()
        question_object = get_object_or_404(queryset, pk=pk)
        if question_object:
            question_object.delete()
        response = Response({
            "status": "Object deleted successfully", 
            "status_code": status.HTTP_404_NOT_FOUND,
        })
        return response
