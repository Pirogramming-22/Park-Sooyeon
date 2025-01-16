from django.urls import path
from . import views

urlpatterns = [
    path('', views.devtool_list, name='devtool_list'),
    path('<int:id>/', views.devtool_detail, name='devtool_detail'),
    path('create/', views.devtool_create, name='devtool_create'),
    path('<int:id>/edit/', views.devtool_edit, name='devtool_edit'),
    path('<int:id>/delete/', views.devtool_delete, name='devtool_delete'),
]