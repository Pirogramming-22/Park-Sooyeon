from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'main/post_list.html', ctx)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    ctx = {'post': post, 'comments': comments, }
    return render(request, 'main/post_detail.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {'form': form}
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {'form': form, }
        return render(request, 'main/post_new.html', ctx)


def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('main:post_detail', pk)
    else:
        form = PostForm(instance=post)
        ctx = {'form': form}
        return render(request, template_name='main/post_new.html', context=ctx)


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('main:post_list')


@csrf_exempt
def like_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get('id')
        action = data.get('type')
        post = Post.objects.get(pk=post_id)

        if action == 'like':
            post.like += 1
        elif action == 'dislike' and post.like > 0:  # 음수로 내려가지 않게 제한
            post.like -= 1
        post.save()

        return JsonResponse({
            'id': post_id,
            'type': action,
            'like_count': max(post.like, 0)  # 음수 값 방어
        })


@csrf_exempt
def new_comment(request):
    req = json.loads(request.body)
    post_id = req['id']
    content = req['content']
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.create(post=post, content=content)
    comment_id = comment.id
    return JsonResponse({'id': post_id, 'content': content, 'comment_id': comment_id})


@csrf_exempt
def delete_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return JsonResponse({'id': comment_id})