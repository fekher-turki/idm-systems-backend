from django.conf.urls import url
from team import views

urlpatterns = [
    url(r'^team/$', views.team_list),
    url(r'^team/(?P<pk>[0-9]+)$', views.team_detail),
    url(r'^team/id/(?P<id>[0-9]+)/$', views.team_list_id),
]