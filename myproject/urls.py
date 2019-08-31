from django.conf.urls import url, include
from django.contrib import admin

from myproject import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^', include('company.urls')),
    url(r'^', include('client.urls')),
    url(r'^', include('clientType.urls')),
    url(r'^', include('country.urls')),
    url(r'^', include('source.urls')),
    url(r'^', include('team.urls')),
    url(r'^', include('sourceTeam.urls')),
    url(r'^', include('sourceType.urls')),
    url(r'^', include('department.urls')),
    url(r'^', include('departmentResponsible.urls')),
    url(r'^', include('employee.urls')),
    url(r'^', include('approver.urls')),
    url(r'^', include('requester.urls')),
    url(r'^', include('approverTeam.urls')),
    url(r'^', include('requesterTeam.urls')),
    url(r'^', include('expenseReport.urls')),
    url(r'^', include('expense.urls')),
    url(r'^', include('currency.urls')),
    url(r'^', include('exchangeRate.urls')),
    url(r'^', include('category.urls')),
    url(r'^', include('expenseStatus.urls')),
    url(r'^', include('rule.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
