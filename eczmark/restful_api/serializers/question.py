
from rest_framework import serializers

from eczmark.models import Question, Grade
from eczmark.restful_api.serializers import (
    SubjectSerializer,
    GradeSerializer,
)

class QuestionSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'user',
            'question_paper',
            'grade',
            'year_uncleaned',
            'cleaned_year',
            'subject',
        ]
    
    def get_subject(self, instance):
        serializer = SubjectSerializer(instance.subject, many=False)
        return serializer.data
    
    def get_grade(self, instance):
        serializer = GradeSerializer(instance.grade, many=False)
        return serializer.data
