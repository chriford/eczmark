
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
        supporting_documents_data = validated_data.pop('attachments', None)
        supporting_links_data = validated_data.pop('links', None)
        if not user_data:
            raise ValueError("Expected data for unnullable fields")
        user = User.objects.create(**user_data)
        
        if not question_data:
            raise ValueError("Expected data for unnullable fields")
        question = Question.objects.create(user=user, **question_data)

        if not supporting_documents_data:
            raise ValueError("Expected data for unnullable fields")
        for document_obj in supporting_documents_data:
            document = Attachment.objects.create(**document_obj)
            question.attachments.add(document)
            question.save()

        if not supporting_links_data:
            raise ValueError("Expected data for unnullable fields")
        for link_obj in supporting_links_data:
            link = Link.objects.create(**link_obj)
            question.links.add(link)
            question.save()
        
        if not validated_data:
            raise ValueError("Expected data for unnullable fields")
        answer = Answer.objects.create(question=question, **validated_data)
        return answer
