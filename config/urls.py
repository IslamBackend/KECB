from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from config.settings.swagger import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/', include('apps.announcement.urls')),
    path('api/v1/', include('apps.center_info.urls')),
    path('api/v1/', include('apps.center_courses.urls')),
    path('api/v1/', include('apps.korean_edu.urls')),
    path('api/v1/', include('apps.library.urls')),
    path('api/v1/', include('apps.home.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
