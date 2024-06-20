from django.contrib import admin
from django.urls import path, include
from users.views import HealthCheckAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Starter Template",
        default_version="v1",
        description="A starter template for Django REST framework projects",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/healthcheck/", HealthCheckAPIView.as_view(), name="healthcheck"),
    path("api/users/", include("users.urls")),
]
