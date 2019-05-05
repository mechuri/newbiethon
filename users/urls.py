from django.urls import path
from . import views

urlpatterns = [
    path('',views.users,name='users'),
    path('login/',views.login,name='login'),
    path('sign_in/',views.sign_in,name='sign_in'),
]