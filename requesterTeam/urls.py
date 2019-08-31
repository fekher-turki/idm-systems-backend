from django.conf.urls import url
from requesterTeam import views

urlpatterns = [
    url(r'^requesterTeam/$', views.requester_team_list),
    url(r'^requesterTeam/(?P<pk>[0-9]+)$', views.requester_team_detail),
    url(r'^requesterTeam/id/(?P<id>[0-9]+)/$', views.requester_team_list_id),
]