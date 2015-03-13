from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'add-good/$', 'acution.commerce.views.add_good', name='add_good'),
)
