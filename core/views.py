from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

def index(request):
    posts = Post.objects.all()[:5]
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)


def blog(request):
    posts = Post.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)

    try:
        obj = paginator.page(page)
    except PageNotAnInteger: 
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    context = {
        'posts':obj
    }
    return render(request, 'blog.html', context)

def detailedView(request, slug):
    posts = Post.objects.get(slug=slug)
    context = {
        'posts':posts
    }
    return render(request, 'detailView.html', context)


def search(request):
    if request.method == 'POST':
        search = request.POST['searched']
        posts = Post.objects.filter(title__contains=search)
        return render(request, 'blog.html', {'posts':posts})
    else:
        posts = Post.objects.all()
        return render(request, 'blog.html',{'posts':posts})