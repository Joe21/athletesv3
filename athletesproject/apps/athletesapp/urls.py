from django.conf.urls import patterns, url

from athletesproject.apps.athletesapp import views

urlpatterns = patterns('',
	# ex: /crud/
	url(r'^$', views.index, name='index'),

	# ex: /crud/5/detail/
	url(r'^(?P<athlete_id>\d+)/$', views.detail, name='detail'),

	# ex: /crud/add/
	url(r'^add/$', views.add, name='add'),

	url(r'^angular/$', views.angular, name='angular')
)