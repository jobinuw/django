from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
		

		url(r'^artists$', views.artists, name='artists'),
		url(r'^artists/(?P<id>\d+)$', views.artistdetails, name='artistdetails'))
		#url(r'^artists/(?P<name>[A-Za-z]+)$', views.artistdetails, name='artistdetails')
		  
		
