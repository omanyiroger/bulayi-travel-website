from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('robots.txt', views.robots, name='robots'),
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/dubai/', views.dubai, name='dubai'),
    path('destinations/zanzibar/', views.zanzibar, name='zanzibar'),
    path('destinations/paris/', views.paris, name='paris'),
    path('destinations/guangzhou/', views.guangzhou, name='guangzhou'),
    path('destinations/nairobi/', views.nairobi, name='nairobi'),
    path('destinations/eldoret/', views.eldoret, name='eldoret'),
    path('destinations/mombasa/', views.mombasa, name='mombasa'),
    path('destinations/kisumu/', views.kisumu, name='kisumu'),
    path('destinations/nakuru/', views.nakuru, name='nakuru'),
]
