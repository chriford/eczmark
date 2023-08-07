
from rest_framework.serializers import ModelSerializer

from eczmark.models import Attachment

class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
