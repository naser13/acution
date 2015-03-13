from django.conf.urls import patterns, include, url
from django.contrib import admin
from acution.commerce.urls import urlpatterns

urlpatterns = patterns('',
                       url(r'^$', include(urlpatterns)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^get/','acution.commerce.views.get'),
                       url(r'^add/','acution.commerce.views.addGood'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'home'},
        name='logout'),

)