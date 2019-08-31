from django.conf.urls import url
from expenseStatus import views

urlpatterns = [
    url(r'^expenseStatus/$', views.expenseStatus_list),
    url(r'^expenseStatus/(?P<pk>[0-9]+)$', views.expenseStatus_detail),
    url(r'^expenseStatus/id/(?P<id>[0-9]+)/$', views.expenseStatus_list_id),
    url(r'^expenseStatus/expense/(?P<expense>[0-9]+)/$', views.expenseStatus_list_expense),
    url(r'^expenseStatus/count/expense/(?P<expense>[0-9]+)/$', views.expenseStatus_list_count),
    url(r'^expenseStatus/mod/(?P<mod>[0-9]+)/expense/(?P<expense>[0-9]+)/$', views.expenseStatus_mod_expense),
]