from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^index/', 'todolists.views.index'),
    url(r'api/', include('todolists.urls')),
    url(r'user/', include('login.urls')),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
)
