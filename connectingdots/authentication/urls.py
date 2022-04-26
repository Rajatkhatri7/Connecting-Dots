from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forget_password', views.forget_password, name='forget_password'),
    




    #testing scripts
    path("register", views.register_request, name="register"),
    path("login_request", views.login_request, name="login_request"),
    


]
