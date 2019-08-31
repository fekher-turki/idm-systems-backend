from django.conf.urls import url
from department import views

urlpatterns = [
    url(r'^department/$', views.department_list),
    url(r'^department/(?P<pk>[0-9]+)$', views.department_detail),
    url(r'^department/id/(?P<id>[0-9]+)/$', views.department_list_id),
]