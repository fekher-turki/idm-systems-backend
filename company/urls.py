from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^company/$', views.company_list),
    # Count expense report
    url(r'^company/count/$', views.countCompany),
    url(r'^company/(?P<pk>[0-9]+)$', views.company_detail),
    url(r'^company/id/(?P<id>[0-9]+)/$', views.company_list_id),
]