
from rest_framework import serializers

from eczmark.models import Answer
from .link import LinkSerializer
from .question import QuestionSerializer
from .attachment import AttachmentSerializer
from .user import UserSerializer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
