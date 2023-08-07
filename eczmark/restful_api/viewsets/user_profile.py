
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from eczmark.models import Profile
from ..serializers import ProfileSerializer

class UserProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
