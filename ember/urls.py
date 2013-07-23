from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers


admin.autodiscover()

urlpatterns = patterns(
    '',
 
    url(r'^$', 'simple.views.index', name='home'),
    # url(r'^ember/', include('ember.foo.urls')),

    # Add zurb foundation resources
    url(r'^foundation/', include('foundation.urls')),

    # Browsable API for debugging
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^rest/', include('restapi.urls')),


    url(r'^admin/', include(admin.site.urls)),
)
