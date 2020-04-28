from django.urls import path, re_path
from api.views import info, service

app_name = 'api'

urlpatterns = [
    # Info routes
    path('info/<int:districtId>/', info.DistrictView.as_view()),
    re_path(r'^info/(?P<latitude>\d+.\d+)/(?P<longitude>\d+.\d+)/$', info.LocationRedirect.as_view()),
    path('info/<str:stateName>/<str:districtName>/', info.NameRedirect.as_view()),

    # Service routes
    path('service/<int:serviceId>/', service.ServiceView.as_view()),
    path('service/', service.EditServiceView.as_view()),
]