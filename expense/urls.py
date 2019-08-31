from django.conf.urls import url
from expense import views

urlpatterns = [
    # list of expense
    url(r'^expense/$', views.expense_list),
    # Count expense report
    url(r'^expense/count/$', views.countExpense),
    # detail of expense
    url(r'^expense/(?P<pk>[0-9]+)$', views.expense_detail),
    # list of expense by user
    url(r'^expense/user/(?P<user>[0-9]+)/$', views.user_expense_list),
    # list of expense by id
    url(r'^expense/id/(?P<id>[0-9]+)/$', views.expense_list_id),
    # list of expense by expenseReport
    url(r'^expense/expenseReport/(?P<expenseReport>[0-9]+)/$', views.expense_list_expense_report),
    # list of expense by expenseReport for specific moderator
    url(r'^expense/(?P<mod>[0-9]+)/expenseReport/(?P<expenseReport_>[0-9]+)/$', views.mod_expense_list_expense_report),
    # list of expense by id for specific user
    url(r'^expense/(?P<user>[0-9]+)/id/(?P<id>[0-9]+)/$', views.expense_detail_user),
]
