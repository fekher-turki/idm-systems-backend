from django.conf.urls import url
from exchangeRate import views

urlpatterns = [
    url(r'^exchangeRate/$', views.exchangeRate_list),
    url(r'^exchangeRate/(?P<pk>[0-9]+)$', views.exchangeRate_detail),
    url(r'^exchangeRate/id/(?P<id>[0-9]+)/$', views.exchangeRate_list_id),
]