from django.shortcuts import render, get_object_or_404, redirect
from .models import DevTool
from ideas.models import Idea

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'devtools/devtool_list.html', {'devtools': devtools})

def devtool_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        kind = request.POST['kind']
        content = request.POST['content']
        DevTool.objects.create(name=name, kind=kind, content=content)
        return redirect('devtool_list')
    return render(request, 'devtools/devtool_form.html')

def devtool_detail(request, id):
    devtool = get_object_or_404(DevTool, id=id)
    related_ideas = Idea.objects.filter(devtool=devtool)  # 해당 개발툴과 연관된 아이디어 필터링
    return render(request, 'devtools/devtool_detail.html', {
        'devtool': devtool,
        'related_ideas': related_ideas
    })

def devtool_edit(request, id):
    devtool = get_object_or_404(DevTool, id=id)
    if request.method == 'POST':
        devtool.name = request.POST['name']
        devtool.kind = request.POST['kind']
        devtool.content = request.POST['content']
        devtool.save()
        return redirect('devtool_list')
    return render(request, 'devtools/devtool_edit.html', {'devtool': devtool})

def devtool_delete(request, id):
    devtool = get_object_or_404(DevTool, id=id)
    devtool.delete()
    return redirect('devtool_list')