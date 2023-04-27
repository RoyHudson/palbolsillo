from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('team', views.team, name='team'),
    path('pal-bolsillo/', views.palbolsillo, name='palbolsillo'),
    path('antojitos', views.antojitos, name='antojitos'),
    path('ubica_tu_super', views.ubicate, name='ubicate'),

]