from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_coins, name='coins'),
    path('<int:coins_id>/', views.coins_detail, name='coins_detail'),
    path('add/', views.add_coins, name='add_coins'),
]
