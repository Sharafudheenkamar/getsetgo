from django.urls import path
from .views import Login,Clubregistration,Eoregistration,Collegeregistration,Schoolregistration

urlpatterns = [
    path('',Login.as_view(),name='Login'),
    path('clubregistration/',Clubregistration.as_view(),name='Clubregistration'),
    path('eoregistration/',Eoregistration.as_view(),name='Eoregistration'),
    path('schoolregistration/',Schoolregistration.as_view(),name='Schoolregistration'),
    path('collegeregistration/',Collegeregistration.as_view(),name='Collegeregistration')
]
