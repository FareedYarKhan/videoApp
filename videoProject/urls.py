
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
admin.site.site_header = "Admin panel"
admin.site.site_title = "Admin panel"
admin.site.index_title = "Welcome to admin panel"
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)