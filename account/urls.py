from django.urls import path
from .views import UserView, authenticate

urlpatterns = [
    path('auth', authenticate),
    path('user', UserView.as_view()),
]