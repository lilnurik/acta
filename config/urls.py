# config/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Swagger схема
schema_view = get_schema_view(
    openapi.Info(
        title="Article Review API",
        default_version='v1',
        description="Документация API для проекта со статьями",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 ПОДКЛЮЧЕНИЕ РОУТОВ ИЗ articles.urls
    path('api/', include('articles.urls')),

    # Swagger UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Медиа
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
