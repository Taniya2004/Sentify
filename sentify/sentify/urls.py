from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),  # Main chat app URLs
    path('ajax/', include('chat.urls_ajax')),  # Include AJAX URLs with prefix
]

if settings.DEBUG:
    for static_dir in settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=static_dir)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
