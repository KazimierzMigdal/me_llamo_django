from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatisticView.as_view(), name='statistics'),
]
