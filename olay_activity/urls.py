from django.conf.urls import patterns,url
from .import views

urlpatterns = patterns('',

    url(r'^$', views.olay_list, name="index"),
    url(r'^package/$', views.activity_olay1,name="olay_package"),
    url(r'^index/$', views.olay_index,name="olay_index"),
)
