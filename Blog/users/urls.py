from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
        path('register/', register, name='registr_url'),
        path('login/', user_login, name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
        path('profile/', profile, name='profile'),
]