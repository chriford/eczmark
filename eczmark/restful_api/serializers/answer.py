
from rest_framework import serializers

from eczmark.models import Answer
from eczmark.restful_api.serializers import (
    LinkSerializer,
    QuestionSerializer,
    AttachmentSerializer,
    UserSerializer,
)

class AnswerSerializer(serializers.ModelSerializer):
    user_obj = serializers.SerializerMethodField()
    attachments_obj = serializers.SerializerMethodField()
    links_obj = serializers.SerializerMethodField()
    question_obj = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            'user',
            'user_obj',
            'question',
            'question_obj',
            'attachments',
            'attachments_obj',
            'links',
            'links_obj',
            'body',
        ]
    
    def get_user_obj(self, instance):
        serializer = UserSerializer(instance.user, many=False)
        return serializer.data

    def get_attachments_obj(self, instance):
        serializer = AttachmentSerializer(instance.attachments, many=True)
        return serializer.data

    def get_links_obj(self, instance):
        serializer = LinkSerializer(instance.links, many=True)
        return serializer.data

    def get_question_obj(self, instance):
        serializer = QuestionSerializer(instance.question, many=False)
        return serializer.data
