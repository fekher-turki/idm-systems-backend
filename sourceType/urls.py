from django.conf.urls import url
from sourceType import views

urlpatterns = [
    url(r'^sourceType/$', views.source_type_list),
    url(r'^sourceType/(?P<pk>[0-9]+)$', views.source_type_detail),
    url(r'^sourceType/id/(?P<id>[0-9]+)/$', views.source_type_list_id),
]