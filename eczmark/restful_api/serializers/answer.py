
from rest_framework import serializers

from eczmark.models import Answer
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
