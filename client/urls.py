from django.conf.urls import url
from client import views

urlpatterns = [
    url(r'^client/$', views.client_list),
    # Count expense report
    url(r'^client/count/$', views.countClient),
    url(r'^client/(?P<pk>[0-9]+)$', views.client_detail),
    url(r'^client/id/(?P<id>[0-9]+)/$', views.client_list_id),
]