from rest_framework import routers
from django.urls import path
from .views import *

router = routers.DefaultRouter()
urlpatterns = [
    path('api/user/<int:tg_id>/', get_user_data),
    path('api/courier/cashin/', accept_courier_cash_in),
    path('api/courier/cashout/', accept_courier_cash_out),
    path('api/courier/', get_all_couriers),
    path('api/dispatcher/', get_all_dispatchers),
    path('api/operators/', get_operators),
    path('api/operators/<int:operator_id>/', get_one_operator)
    ] + router.urls
