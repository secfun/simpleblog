# -*- coding:utf-8 -*-
from django.core.paginator import Paginator
from django.db.models import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.shortcuts import render, Http404
from django.views.decorators.csrf import csrf_exempt

from blog.models import Article, Comment


# Create your views here.


def index(request, page):
    articles = Article.objects.order_by("created_at")
    pager = Paginator(articles, 10)
    page = int(page)
    page = 0 if not page or page < 0 else page
    page = pager.num_pages - 1 if page > pager.num_pages - 1 else page
    return render(request, 'index.html', {'articles': pager.page(page + 1)})


def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except ObjectDoesNotExist:
        return Http404
    return render(request, 'article_detail.html', {'article': article})


@csrf_exempt
def comment_add(request):
    article_id = request.POST.get('article')
    title = request.POST.get('title')
    content = request.POST.get('content')
    try:
        article = Article.objects.get(id=article_id)
    except ObjectDoesNotExist:
        return JsonResponse({"success": False, "msg": "article not found"})

    Comment.objects.create(name=title, comment=content, article=article)

    return JsonResponse({"success": True, "msg": ""})
