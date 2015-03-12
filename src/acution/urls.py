from django.conf.urls import patterns, include, url
from django.contrib import admin
from acution.commerce.urls import urlpatterns

urlpatterns = patterns('',
                       url(r'^$', include(urlpatterns)),
                       url(r'^admin/', include(admin.site.urls)),
)
