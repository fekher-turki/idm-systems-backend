from django.conf.urls import url
from approver import views

urlpatterns = [
    url(r'^approver/$', views.approver_list),
    url(r'^approver/(?P<pk>[0-9]+)$', views.approver_detail),
    url(r'^approver/id/(?P<id>[0-9]+)/$', views.approver_list_id),
    url(r'^approver/user/(?P<user>[0-9]+)/$', views.approver_list_user),
]