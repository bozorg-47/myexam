from django.urls import path
from .views import mycar_list
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('mycar/', views.mycar_list, name='mycar_list'),
    path('mainpage/details/<int:id>', views.details, name='details'),

]