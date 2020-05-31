from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


# schema view description for swagger
schema_view = get_schema_view(
   openapi.Info(
      title="FullThrottle API",
      default_version='v1',
      description="An assignment by FullThrottle Lab.",
      contact=openapi.Contact(email="raushan.br.in@gmail.com"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

# Admin schema customization
admin.site.site_header = "FullThrottle Lab Admin"
admin.site.site_title = "FullThrottle Assignment"
admin.site.index_title = "An assignment by FullThrottle Lab."


urlpatterns = [
    path('admin/', admin.site.urls),
    path('activity/', include('activity.urls')),
]

urlpatterns += [
   path('', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
]
