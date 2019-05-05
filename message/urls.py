from django.urls import path, include
from . import views

urlpatterns = [
    path('message/',views.message,name='message'),
]