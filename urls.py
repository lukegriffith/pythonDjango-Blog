
from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<number>\d+)/$', views.testing, name='testing'),
	url(r'^posts$', views.RecentPosts, name='RecentPosts')
)

