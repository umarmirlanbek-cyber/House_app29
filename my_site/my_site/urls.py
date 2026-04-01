from django.contrib import admin
from django.urls import include,path
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="HOUSE_APP_RAKANBEK&UMAR",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apart_app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('accounts/', include('allauth.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]