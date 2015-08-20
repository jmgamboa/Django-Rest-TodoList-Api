from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from login import views

urlpatterns = patterns('',
	url(r'^register/$', views.CreateUserView.as_view()),
	url(r'^login/$', views.AuthView.as_view(), name='authenticate'),
	url(r'^logout/$', 'login.views.logout'),
	)
