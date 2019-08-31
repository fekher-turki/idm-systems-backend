from django.conf.urls import include, url
from rest_framework import routers
from api import views
from api.views import CustomObtainAuthToken

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', CustomObtainAuthToken.as_view()),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^users/id/(?P<id>[0-9]+)/$', views.user_list_id),
    url(r'^users/type/(?P<user_type>[0-9]+)/$', views.user_list_type),
]