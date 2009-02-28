from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('apps.core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.SERVER_ENV == 'development':
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

