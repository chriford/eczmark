from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from drf_yasg2 import openapi
from rest_framework import permissions
from drf_yasg2.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="ECZ Marked API",
        default_version="v3",
        description="The UI for clean view of restful APIs for the ECZ Marked project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eczmark.core_urls', namespace='eczmark')),
    path('auth/', include('eczmark.auth_urls', namespace='auth')),
] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
