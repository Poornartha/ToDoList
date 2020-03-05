from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),

    path('index/<str:pk>/', views.index, name="index"),
    path('update_task/<str:cpk>/<str:tpk>/', views.update_task, name="update_task"),
    path('delete_task/<str:cpk>/<str:tpk>/', views.delete_task, name="delete_task"),

]