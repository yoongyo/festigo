from django.contrib import admin
from django.urls import re_path, include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    re_path(r'^admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    re_path(r'^festival/', include(('festival.urls', 'festival'), namespace='festival')),
]


urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.views import static
static_list = [
 (settings.STATIC_URL, settings.STATIC_ROOT),
 (settings.MEDIA_URL, settings.MEDIA_ROOT),
]
for (prefix_url, root) in static_list:
    if '://' not in prefix_url: # 외부 서버에서 서빙하는 것이 아니라면
        prefix_url = prefix_url.lstrip('/')
        url_pattern = r'^' + prefix_url + r'(?P<path>.+)'
        pattern = re_path(url_pattern, static.serve, kwargs={'document_root': root})
        urlpatterns.append(pattern)