from django.urls import path
from . import views

app_name = 'ReviewList'

urlpatterns = [
    path('', views.review_list, name='review_list'),  # 리뷰 리스트
    path('<int:id>/', views.review_detail, name='review_detail'),  # 리뷰 디테일
    path('new/', views.review_create, name='review_create'),  # 새 리뷰 작성
    path('<int:id>/edit/', views.review_update, name='review_update'),  # 리뷰 수정
    path('<int:id>/delete/', views.review_delete, name='review_delete'),  # 리뷰 삭제
]