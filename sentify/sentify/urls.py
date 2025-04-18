from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('', include('chat.urls_ajax')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
'''