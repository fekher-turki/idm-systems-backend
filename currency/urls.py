from django.conf.urls import url
from currency import views

urlpatterns = [
    url(r'^currency/$', views.currency_list),
    url(r'^currency/(?P<pk>[0-9]+)$', views.currency_detail),
    url(r'^currency/id/(?P<id>[0-9]+)/$', views.currency_list_id),
]