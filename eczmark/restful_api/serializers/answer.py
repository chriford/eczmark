
from rest_framework import serializers

from eczmark.models import Answer, User, Attachment, Link, Question
from .link import LinkSerializer
from .question import QuestionSerializer
from .attachment import AttachmentSerializer
from .user import UserSerializer

class AnswerSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer()
    question = QuestionSerializer()
    user = UserSerializer()
    
    class Meta:
        model = Answer
        fields = [
            'user',
            'question',
            'attachments',
            'links',
            'body',
        ]
    
    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        question_data = validated_data.pop('question', None)
        if not user_data:
            raise ValueError("Expected data for unnullable fields")
        user = User.objects.create(**user_data)
        
        if not question_data:
            raise ValueError("Expected data for unnullable fields")
        question = Question.objects.create(user=user, **question_data)
        
        if not validated_data:
            raise ValueError("Expected data for unnullable fields")
        answer = Answer.objects.create(question=question, **validated_data)
        return answer
        