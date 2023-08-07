from rest_framework.routers import DefaultRouter

from eczmark.restful_api.viewsets  import (
    AnswerViewSet,
    QuestionViewSet,
    ReportViewSet,
)

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'questions', AnswerViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')
router.register(r'reports', AnswerViewSet, basename='report')
=======
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')
router.register(r'reports', ReportViewSet, basename='report')
>>>>>>> implement-model-viesets

app_name = 'eczmark'
urlpatterns = router.urls
