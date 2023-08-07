
from rest_framework.serializers import ModelSerializer

from eczmark.models import Question
from eczmark.restful_api.serializers import (
    UserSerializer,
    SubjectSerializer,
    GradeSerializer,
)

class QuestionSerializer(ModelSerializer):
    user = UserSerializer()
    subject = SubjectSerializer()
    grade = GradeSerializer()
    
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
