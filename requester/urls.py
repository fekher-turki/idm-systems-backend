from django.conf.urls import url
from requester import views

urlpatterns = [
    url(r'^requester/$', views.requester_list),
    url(r'^requester/(?P<pk>[0-9]+)$', views.requester_detail),
    url(r'^requester/id/(?P<id>[0-9]+)/$', views.requester_list_id),
]