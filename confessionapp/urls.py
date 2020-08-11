from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('postpage/', views.postpage, name='postpage'),
    path('creatpost/', views.creatpost, name ='creatpost'),
]
