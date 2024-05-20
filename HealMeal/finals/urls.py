from django.urls import path
from . import views

urlpatterns = [
    path('finals/', views.finals, name='finals')
]