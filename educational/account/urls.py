from django.urls import path
from . import views


urlpatterns = [
    path('', views.entrance),
    path('registration', views.registration)
]
