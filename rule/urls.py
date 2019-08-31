from django.conf.urls import url
from rule import views

urlpatterns = [
    url(r'^rule/$', views.rule_list),
    url(r'^rule/(?P<pk>[0-9]+)$', views.rule_detail),
    url(r'^rule/id/(?P<id>[0-9]+)/$', views.rule_list_id),
]