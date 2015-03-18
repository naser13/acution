from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^add/$','acution.commerce.views.add_good'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'},
                           name='login'),

                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': 'home'},
                           name='logout'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'acution.commerce.views.home', name='home'),
                       url(r'^addgood/$','acution.commerce.views.add_good'),
                       url(r'^goods/$','acution.commerce.views.good')
    )+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

