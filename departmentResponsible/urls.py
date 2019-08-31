from django.conf.urls import url
from departmentResponsible import views

urlpatterns = [
    url(r'^departmentResponsible/$', views.department_responsible_list),
    url(r'^departmentResponsible/(?P<pk>[0-9]+)$', views.department_responsible_detail),
    url(r'^departmentResponsible/id/(?P<id>[0-9]+)/$', views.department_responsible_list_id),
]