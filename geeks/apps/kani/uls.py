from django.urls import path

from apps.kani.views import *

urlpatterns = [
    path('', index, name="index"),
]