
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Courses site",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('courses_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
