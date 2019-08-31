from django.conf.urls import url
from source import views

urlpatterns = [
    url(r'^source/$', views.source_list),
    url(r'^source/(?P<pk>[0-9]+)$', views.source_detail),
    url(r'^source/id/(?P<id>[0-9]+)/$', views.source_list_id),
]