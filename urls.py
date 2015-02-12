
from django.conf.urls import patterns, url

from blogsite import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<entry_id>\d+)/$', views.Posts, name='Posts'),
	url(r'^(?P<categoryChoice>\d+)/Category/$', views.Categories, name='CategoryView')
)
