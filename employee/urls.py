from django.conf.urls import url
from employee import views

urlpatterns = [
    url(r'^employee/$', views.employee_list),
    url(r'^employee/(?P<pk>[0-9]+)$', views.employee_detail),
    url(r'^employee/id/(?P<id>[0-9]+)/$', views.employee_list_id),
    url(r'^employee/user/(?P<id>[0-9]+)/$', views.employee_user_id),
    url(r'^employee/approver/$', views.employee_approver),
]