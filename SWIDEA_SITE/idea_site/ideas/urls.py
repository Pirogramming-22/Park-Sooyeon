from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('<int:id>/', views.idea_detail, name='idea_detail'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:id>/edit/', views.idea_edit, name='idea_edit'),
    path('<int:id>/delete/', views.idea_delete, name='idea_delete'),
    path('<int:id>/update_interest/', views.update_interest, name='update_interest'),
]