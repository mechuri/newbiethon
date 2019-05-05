from django.urls import path
from . import views

urlpatterns=[
    path('match/', views.match, name="match"),
    path('complete/', views.complete, name="complete"),
    path('fail/', views.fail, name="fail"),
    path('all_users', views.all_users, name="all_users"),
    path('chat/<str:room_num>',views.send_index,name="send_index"),
    
    ]