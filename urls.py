from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^wx/$', 'weixin.views.home', name='home'),
    # url(r'^syaweb/', include('syaweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^vote/', 'vote.views.vote', name='vote'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)
