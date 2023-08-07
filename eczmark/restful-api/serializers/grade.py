
from rest_framework.serializers import ModelSerializer

from eczmark.models import Grade

class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
