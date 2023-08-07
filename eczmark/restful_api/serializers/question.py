
from rest_framework.serializers import ModelSerializer

from eczmark.models import Question, Grade, User, Subject

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
    
    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        grade_data = validated_data.pop('grade', None)
        subject_data = validated_data.pop('subject', None)

        if not user_data:
            raise ValueError("Expected data for unnullable fields")
        user = User.objects.create(**user_data)
        
        if not subject_data:
            raise ValueError("Expected data for unnullable fields")
        subject = Subject.objects.create(**subject_data)
        
        if not grade_data:
            raise ValueError("Expected data for unnullable fields")
        grade = Grade.objects.create(**grade_data)
        
        if not validated_data:
            raise ValueError("Expected data for unnullable fields")
        question = Question.objects.create(user=user, subject=subject, grade=grade, **validated_data)
        return question
        
