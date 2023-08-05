from rest_framework.routers import DefaultRouter

from eczmark.restful_api.viewsets  import (
    AnswerViewSet,
)

router = DefaultRouter()
router.register(r'answers', AnswerViewSet, basename='answer')

urlpatterns = router.urls
