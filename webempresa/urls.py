
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
]


if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)