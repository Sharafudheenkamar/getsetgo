from django.urls import path
from .views import *
urlpatterns = [
   path('viewadministratordashboard/',Viewadminsistratordashoard.as_view(),name='viewadministratordashboard'),
   path('viewclub/',Viewclub.as_view(),name='viewclub'),
   path('viewschool/',Viewschool.as_view(),name='viewschool'),
   path('viewcollege/',Viewcollege.as_view(),name='viewcollege'),
   path('editcollege/<int:id>/',Editcollege.as_view(),name='editcollege'),
   path('deletecollege/<int:id>/',Deletecollege.as_view(),name='deletecollege'),
   path('editschool/<int:id>/',Editschool.as_view(),name='editschool'),
   path('deleteschool/<int:id>/',Deleteschool.as_view(),name='deleteschool'),
]
