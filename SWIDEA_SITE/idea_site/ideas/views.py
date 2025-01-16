from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Idea
from devtools.models import DevTool
from django.http import JsonResponse
import json

def idea_list(request):
    sort = request.GET.get('sort', 'latest')  
    ideas = Idea.objects.all()

    if sort == 'starred':
        
        ideas = ideas.annotate(
            is_starred_order=ExpressionWrapper(
                models.F('is_starred'), output_field=BooleanField()
            )
        ).order_by('-is_starred_order', '-created_at')
    elif sort == 'interest':
        # 관심도 높은 순 정렬
        ideas = ideas.order_by('-interest', '-created_at')
    elif sort == 'name':
        # 제목 순 정렬
        ideas = ideas.order_by('title')
    else:
        # 최신순 정렬
        ideas = ideas.order_by('-created_at')
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

def update_interest(request, idea_id):
    if request.method == 'POST':
        try:
            idea = Idea.objects.get(id=idea_id)
            data = json.loads(request.body) 
            action = data.get('action')

            print(f"Action: {action}, Idea ID: {idea_id}")  

            if action == 'increase':
                idea.interest += 1
            elif action == 'decrease':
                idea.interest = max(0, idea.interest - 1)  # 관심도는 0 이상으로 유지

            idea.save() 
            print(f"New interest: {idea.interest}")
            return JsonResponse({'new_interest': idea.interest})
        except Idea.DoesNotExist:
            print("Idea not found")
            return JsonResponse({'error': 'Idea not found'}, status=404)
    print("Invalid request method")
    return JsonResponse({'error': 'Invalid request method'}, status=400)

#찜하기 버튼
def toggle_star(request, id):
    if request.method == 'POST':
        idea = Idea.objects.get(id=id)
        idea.is_starred = not idea.is_starred
        idea.save()
        return JsonResponse({'is_starred': idea.is_starred})