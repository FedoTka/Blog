from django.urls import path

from .views import *

urlpatterns = [
        path('', register, name='registr_url'),
]