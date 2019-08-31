from django.conf.urls import url
from sourceTeam import views

urlpatterns = [
    url(r'^sourceTeam/$', views.source_team_list),
    url(r'^sourceTeam/(?P<pk>[0-9]+)$', views.source_team_detail),
    url(r'^sourceTeam/id/(?P<id>[0-9]+)/$', views.source_team_list_id),
]