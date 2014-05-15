from django.conf.urls import patterns, include, url
from views import search, search_submit

urlpatterns = patterns('',
    url(r'^$', search),
    url(r'^submit/$', search_submit)
)
