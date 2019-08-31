from django.conf.urls import url
from country import views

urlpatterns = [
    url(r'^country/$', views.country_list),
    url(r'^country/(?P<pk>[0-9]+)$', views.country_detail),
    url(r'^country/id/(?P<id>[0-9]+)/$', views.country_list_id),
]