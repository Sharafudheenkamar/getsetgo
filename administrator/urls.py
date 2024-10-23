from django.urls import path
from .views import Viewadminsistratordashoard
urlpatterns = [
   path('viewadministratordashboard/',Viewadminsistratordashoard.as_view(),name='viewadministratordashboard'),
]
