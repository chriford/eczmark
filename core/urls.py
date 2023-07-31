
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eczmark.core_urls', namespace='eczmark')),
    path('auth/', include('eczmark.auth_urls', namespace='auth')),
]