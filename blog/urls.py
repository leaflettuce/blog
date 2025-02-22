from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^names_search$', views.names_search, name='names_search'),
	url(r'^us_births$', views.us_births, name='us_births'),
	url(r'^tdwp_shows$', views.tdwp_shows, name='tdwp_shows'),
	url(r'^goodreads_exploration$', views.goodreads_exploration, name='goodreads_exploration'),]