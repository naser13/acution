from django.conf.urls import patterns, include, url
from django.contrib import admin
from acution.commerce.urls import urlpatterns

urlpatterns = patterns('',
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'},
                           name='login'),

                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': 'home'},
                           name='logout'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^commerce/', include(urlpatterns)),
                       url(r'^$', 'acution.commerce.views.home', name='home'),
    )