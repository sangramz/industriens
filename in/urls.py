from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('kunde/', views.kunde, name='kunde'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('betal/', views.betal, name='betal'),
    path('afdrag/', views.afdrag, name='afdrag'),
    path('modtaget/', views.modtaget, name='modtaget'),
    path('customer_db/', views.customer_db, name='customer_db'),
]
