from django.urls import path
from .views import SignUpView, LoginUser, account, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registration', SignUpView.as_view(), name='registration'),
    path('', LoginUser.as_view(), name='entrance'),
    path('profile', account, name='profile'),
    path('profile-changed', profile, name='profile-changed'),
]
