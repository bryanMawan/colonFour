from django.urls import path
from .views import TestView, login_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', TestView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
