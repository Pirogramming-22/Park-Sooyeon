from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Review

# 리뷰 리스트
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

# 리뷰 디테일
def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    return render(request, 'review_detail.html', {'review': review})

# 리뷰 작성
def review_create(request):
    if request.method == 'POST':
        Review.objects.create(
            title=request.POST['title'],
            release_year=request.POST['release_year'],
            director=request.POST['director'],
            main_actor=request.POST['main_actor'],
            genre=request.POST['genre'],
            rating=request.POST['rating'],
            runtime=request.POST['runtime'],
            content=request.POST['content'],
        )
        return redirect('ReviewList:review_list')
    return render(request, 'review_form.html')

# 리뷰 수정
def review_update(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        review.title = request.POST['title']
        review.release_year = request.POST['release_year']
        review.director = request.POST['director']
        review.main_actor = request.POST['main_actor']
        review.genre = request.POST['genre']
        review.rating = request.POST['rating']
        review.runtime = request.POST['runtime']
        review.content = request.POST['content']
        review.save()
        return redirect('ReviewList:review_detail', id=review.id)
    return render(request, 'review_form.html', {'review': review})

# 리뷰 삭제
def review_delete(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('ReviewList:review_list')
