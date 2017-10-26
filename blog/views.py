from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.generic.dates import ArchiveIndexView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models.aggregates import Count
from blog.models import Article
from blog.models import Category
from blog.models import Tag

# Create your views here.
def index(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'index.html', {'post_list' : post_list})

def article(request, id):
    post = Article.objects.get(id=id)
    return render(request, 'article.html', {'post': post})

def category(request, name):
    category = Category.objects.get(name=name)
    post_list = Article.objects.filter(category_id=category.id)
    return render(request, 'category.html', {'category': category, 'post_list': post_list})

def tag(request, name):
    tag = Tag.objects.get(name=name)
    post_list = Article.objects.filter(tag_id=tag.id)
    return render(request, 'tag.html', {'tag': tag, 'post_list': post_list})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoseNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})

def categories(request):
    try:
        category_list = Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
    except Category.DoseNotExist:
        raise Http404
    return render(request, 'categories.html', {'category_list': category_list, 'error': False})

def tags(request):
    try:
        tag_list = Tag.objects.all()
    except Tag.DoseNotExist:
        raise Http404
    return render(request, 'tags.html', {'tag_list': tag_list, 'error': False})

def about(request):
    return render(request, 'about.html')

def page_not_found(request):
    return render(request, '404.html')

class ArticleArchiveView(ArchiveIndexView):
    make_object_list = True
    allow_empty = True
    allow_future = True
    date_field = 'date_time'
    context_object_name = 'post_list'
    template_name = 'archives.html'
    paginate_by = 10
    queryset = Article.objects.all()
