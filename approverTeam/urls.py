from django.conf.urls import url
from approverTeam import views

urlpatterns = [
    url(r'^approverTeam/$', views.approver_team_list),
    url(r'^approverTeam/(?P<pk>[0-9]+)$', views.approver_team_detail),
    url(r'^approverTeam/id/(?P<id>[0-9]+)/$', views.approver_team_list_id),
]