# -*- coding:utf-8 -*-
from django.shortcuts import render, Http404, HttpResponse
from blog.models import Article, Comment
from django.db.models import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    articles = Article.objects.order_by("created_at")[:10]
    return render(request, 'index.html', {'articles': articles})


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
