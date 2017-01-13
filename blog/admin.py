# -*- coding:utf-8 -*-
from django.contrib import admin

from blog.models import Article, Comment


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'article']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
