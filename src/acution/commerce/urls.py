from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'acution.commerce.views.home', name='home'),
)
