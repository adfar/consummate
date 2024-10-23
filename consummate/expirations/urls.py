from django.urls import path

from expirations import views

urlpatterns = [
    path('', views.expirations, name='expirations'),
]