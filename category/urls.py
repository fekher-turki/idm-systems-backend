from django.conf.urls import url
from category import views

urlpatterns = [
    url(r'^category/$', views.category_list),
    url(r'^category/(?P<pk>[0-9]+)$', views.category_detail),
    url(r'^category/id/(?P<id>[0-9]+)/$', views.category_list_id),
]