from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

]
