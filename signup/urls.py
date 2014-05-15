from django.conf.urls import patterns, include, url
from views import signup_form, signup_submit, check_username, code, decode

urlpatterns = patterns('',
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './templates/js/'} ),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './templates/css/'} ),
    url(r'^$', signup_form),
    url(r'^submit/$', signup_submit),
    url(r'^check_username/$', check_username),
    url(r'^code/$', code),
    url(r'^decode/$', decode),
)
