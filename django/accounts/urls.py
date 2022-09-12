from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/<str:message>/', auth_views.LoginView.as_view(), name='login-with-message'),
    path('register/', views.RegisterView.as_view(), name="accounts-register"),
]