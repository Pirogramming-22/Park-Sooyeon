from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('new_comment/', views.new_comment, name='new_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/post_edit/', views.post_edit, name='post_edit'),

]
