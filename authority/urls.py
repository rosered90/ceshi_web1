from django.conf.urls import patterns,url
from .import views

urlpatterns = patterns('',
	url('^$', views.index_base, name="base"),
    # url('^index/$', views.index, name="index"),
    # url('^detai/$', views.detail, name="detail"),
)