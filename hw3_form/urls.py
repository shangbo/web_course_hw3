from django.conf.urls import patterns, include, url

from django.contrib import admin
from signup import urls as signup_urls
from login import urls as login_urls
from login.views import login as login_login
from search import urls as search_urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './templates/js/'} ),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './templates/css/'} ),
    url(r'^photos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './photos/'}),
    url(r'^$', login_login),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', include(signup_urls)),
    url(r'^login/', include(login_urls)),
    url(r'^search/', include(search_urls)),
)
