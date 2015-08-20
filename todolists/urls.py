from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from todolists import views

urlpatterns = patterns('',
	url(r'^todo/$', views.TodoListView.as_view()),
	url(r'^todo/(?P<pk>[0-9]+)/$', views.TodoListDetailView.as_view()),
	url(r'^todoitem/$', views.TodoItemView.as_view()),	
	url(r'^todoitem/(?P<pk>[0-9]+)/$', views.TodoItemSingleView.as_view()),
	)

# extentiosn givne will return the appropriate format
urlpatterns = format_suffix_patterns(urlpatterns)