from django.urls import  path

from user import views

urlpatterns = [
    path('', views.utilisateur, name='accueil'),
    path('utilisateurs/', views.utilisateur, name='utilisateur'),
    path('inscription/', views.inscription_views, name='inscription'),
]
