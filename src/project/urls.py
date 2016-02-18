from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings
import os.path

admin.autodiscover()

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^err/404', TemplateView.as_view(template_name="404.html"), name='err-404'),
    url(r'^err/500', TemplateView.as_view(template_name="500.html"), name='err-500'),
    url(r'', include('apps.app.urls')),
]

if settings.LOCAL_DEV:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=os.path.join(settings.MEDIA_ROOT))
