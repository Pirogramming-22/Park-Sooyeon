from django.db import models

class Review(models.Model):
    title = models.TextField()  # 영화 제목
    release_year = models.IntegerField(null=True, blank=True) #개봉년도
    director = models.TextField()  # 감독
    main_actor = models.TextField()  # 주연
    genre = models.TextField()  # 장르
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # 별점
    runtime = models.IntegerField()  # 러닝타임 분으로 표기
    content = models.TextField()  # 리뷰 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일

def __str__(self):
    return self.title