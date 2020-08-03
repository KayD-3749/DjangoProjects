from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Numbers', views.get_nums)
]
