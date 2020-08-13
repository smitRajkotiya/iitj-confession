from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('postpage/', views.postpage, name='postpage'),
    path('creatpost/', views.creatpost, name ='creatpost'),
    path('contactus/', views.contactus, name ='contactus'),
    path('aboutus/', views.aboutus, name ='aboutus'),
    path('profilepage/', views.profilepage, name='profilepage'),

]
