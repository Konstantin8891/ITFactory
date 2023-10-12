from django.urls import path

from .views import (
    AddUserAPIView, AddShopAPIView, EmployeeShopsAPIView, VisitShopAPIView
)

app_name = 'api'

urlpatterns = [
    path('add_user/', AddUserAPIView.as_view(), name='add_user'),
    path('add_shop/', AddShopAPIView.as_view(), name='add_shop'),
    path('get_shops/', EmployeeShopsAPIView.as_view(), name='get_shops'),
    path('visit_shop/', VisitShopAPIView.as_view(), name='visit_shop'),
]
