from users.apps import UsersConfig
from django.urls import path

from . import views

app_name = UsersConfig.name

urlpatterns = [
       path('', views.home, name='home'),
       # path('about/', views.about, name='about'),
   ]