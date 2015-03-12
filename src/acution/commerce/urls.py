from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'commerce.views.home', name='home'),
)
