from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.users,name='users'),
    path('login/',views.login,name='login'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('bye/<int:id>', views.bye, name="bye"),
    path('quit/', views.quit, name="quit"),
    path('password/<int:id>',views.password,name='password'),
    path('mypage/<int:id>', views.mypage, name="mypage"),
    path('check/', views.check, name="check"),
    path('update/<int:id>', views.update, name="update"),
    

]