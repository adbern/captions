from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#root urls
#url(regex, view, kwargs, name)
urlpatterns = patterns('',
    url(r'^captions/youtubeid=', include('captions.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
