from django.conf.urls import url
from clientType import views

urlpatterns = [
    url(r'^clientType/$', views.client_type_list),
    url(r'^clientType/(?P<pk>[0-9]+)$', views.client_type_detail),
    url(r'^clientType/id/(?P<id>[0-9]+)/$', views.client_type_list_id),
]