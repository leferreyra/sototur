from django.conf.urls import patterns, include, url
from django.conf import settings
from website.views import HomeBlockList, CategoryPackagesList, PackageDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sototur.views.home', name='home'),
    url(r'^$', HomeBlockList.as_view()),
    url(r'^paquetes/(?P<pk>\d+)$', CategoryPackagesList.as_view(), name='category_view'),
    url(r'^paquete/(?P<pk>\d+)$', PackageDetail.as_view(), name='package_view'),
    url(r'^admin/', include(admin.site.urls)),
)


# Serving static files in development
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
