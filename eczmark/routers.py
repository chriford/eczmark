from rest_framework.routers import DefaultRouter

from eczmark.restful_api.viewsets  import (
    AnswerViewSet,
    QuestionViewSet,
    ReportViewSet,
)

router = DefaultRouter()
router.register(r'questions', AnswerViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')
router.register(r'reports', AnswerViewSet, basename='report')

urlpatterns = router.urls
