from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('home',views.home,name='Home'),
    path('shop',views.shop,name='shop'),
    path('login',views.Login,name='Login'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('SignUpSuccess',views.SignUpSuccess,name='SignUpSuccess'),
    path('SignInSuccess',views.SignInSuccess,name='SignInSuccess'),
    path('SignUnSuccess',views.SignUnSuccess,name='SignUnSuccess'),
]