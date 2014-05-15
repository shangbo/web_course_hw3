from django.conf.urls import patterns, include, url
from views import login, code, login_submit, decode, modified, modified_submit
urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^code/$', code),
    url(r'^submit/$', login_submit),
    url(r'^submit/photos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './photos/'}),
    url(r'^decode/$', decode),
    url(r'^modified/$', modified),
    url(r'^modified/$', modified),
    url(r'^modified/submit/$', modified_submit),
)