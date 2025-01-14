from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Idea
from devtools.models import DevTool
from django.http import JsonResponse

#아이디어 리스트 
def idea_list(request):
    sort = request.GET.get('sort', 'latest')
    if sort == 'latest':
        ideas = Idea.objects.order_by('-created_at')
    elif sort == 'starred':
        ideas = Idea.objects.filter(is_starred=True)
    elif sort == 'name':
        ideas = Idea.objects.order_by('title')
    elif sort == 'interest':
        ideas = Idea.objects.order_by('-interest')
    else:
        ideas = Idea.objects.all()
    return render(request, 'ideas/idea_list.html', {'ideas': ideas, 'sort': sort})

#아이디어 상세설명
def idea_detail(request, id):
    idea = get_object_or_404(Idea, id=id)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

#아이디어 생성
def idea_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        interest = int(request.POST['interest'])
        devtool_id = int(request.POST['devtool'])
        image = request.FILES['image'] if 'image' in request.FILES else None

        devtool = DevTool.objects.get(id=devtool_id)

        Idea.objects.create(
            title=title,
            content=content,
            interest=interest,
            devtool=devtool,
            image=image
        )
        return redirect('idea_list')
    devtools = DevTool.objects.all()
    return render(request, 'ideas/idea_form.html', {'devtools': devtools})

#아이디어 수정
def idea_edit(request, id):

    idea = get_object_or_404(Idea, id=id)

    if request.method == 'POST':
        
        idea.title = request.POST['title']
        idea.content = request.POST['content']
        idea.interest = request.POST['interest']
        idea.devtool = DevTool.objects.get(id=request.POST['devtool'])

        if 'image' in request.FILES:
            idea.image = request.FILES['image'] if 'image' in request.FILES else None
        
        idea.save()
        return redirect('idea_detail', id=idea.id) 
    devtools = DevTool.objects.all()
    return render(request, 'ideas/idea_edit.html', {'idea': idea, 'devtools': devtools})

#아이디어 삭제 
def idea_delete(request, id):
    idea = get_object_or_404(Idea, id=id)
    idea.delete()
    return redirect('idea_list')

#관심도 조정
def update_interest(request, id):
    idea = Idea.objects.get(id=id)
    action = request.POST.get('action')
    if action == 'increase':
        idea.interest += 1
    elif action == 'decrease' and idea.interest > 0:
        idea.interest -= 1
    idea.save()
    return JsonResponse({'interest': idea.interest})