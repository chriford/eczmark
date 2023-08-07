
from rest_framework.serializers import ModelSerializer

from eczmark.models import Question

from .user import UserSerializer
from .subject import SubjectSerializer
from .grade import GradeSerializer

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
