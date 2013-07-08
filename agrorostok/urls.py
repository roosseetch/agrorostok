from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from istore.app import shop

# These need to be imported into this namespace
from istore.views import handler500, handler404, handler403

# Uncomment the next two lines to enable the admin:
admin.autodiscover()


urlpatterns = patterns('',
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/',
                       # include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin_tools/', include('admin_tools.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'', include(shop.urls)),
                      (r'^contact$', TemplateView.as_view(
                          template_name='contact.html'),  {}, 'contact'),
                       )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('',
                            # (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            #  {'document_root': static}),
                           (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
                            url(r'^404$', TemplateView.as_view(
                                template_name='404.html')),
                            url(r'^500$', TemplateView.as_view(
                                template_name='500.html')),
                            )
