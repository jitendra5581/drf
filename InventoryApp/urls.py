from django.urls import path
from .views import *



urlpatterns = [
    path('get-inventory/', GetServerDetails.as_view()),
    path('get-server/', GetServer.as_view()),
]
