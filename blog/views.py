from django.shortcuts import render, Http404, HttpResponse
from blog.models import Article
from django.db.models import ObjectDoesNotExist

# Create your views here.


def index(request):
    articles = Article.objects.order_by("created_at")[:10]
    return render(request, 'index.html', {'articles': articles})


def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except ObjectDoesNotExist:
        return Http404
    return HttpResponse(article.title)
