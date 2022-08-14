from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout,name="logout"),
    path('header',views.header,name="header"),
    path('snews',views.snews,name="snews"),
    
]