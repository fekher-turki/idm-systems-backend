from django.conf.urls import url
from expenseReport import views

urlpatterns = [
    # list of expense report
    url(r'^expenseReport/$', views.expenseReport_list),
    # Count expense report
    url(r'^expenseReport/count/$', views.countExpenseReport),
    # detail of expense report
    url(r'^expenseReport/(?P<pk>[0-9]+)$', views.expenseReport_detail),
    # list of expense report by id
    url(r'^expenseReport/id/(?P<id>[0-9]+)/$', views.expenseReport_list_id),
    # list of expense report for specific user
    url(r'^expenseReport/user/(?P<user>[0-9]+)/$', views.expenseReport_list_user),
    # list of expense report for specific moderator
    url(r'^expenseReport/mod/(?P<mod>[0-9]+)/$', views.expenseReport_list_mod),
    # list of expense report by for specific moderator
    url(r'^expenseReport/(?P<id>[0-9]+)/mod/(?P<mod>[0-9]+)/$', views.expenseReport_detail_mod),
    # list of expense report for specific user
    url(r'^expenseReport/(?P<id>[0-9]+)/user/(?P<user>[0-9]+)/$', views.expenseReport_detail_user),
    # count number of approver per expense report by id
    url(r'^expenseReport/id/(?P<id>[0-9]+)/approvers/$', views.expenseReport_count),
]
