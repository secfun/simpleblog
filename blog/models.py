# -*- coding:utf-8 -*-

from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.TextField(help_text=u"标题")
    image = models.ImageField(help_text=u"图片")
    content = models.TextField(help_text=u"内容")
    created_at = models.DateTimeField(help_text=u"创建时间", auto_now_add=True)


class Comment(models.Model):
    name = models.TextField(help_text=u"评论标题")
    comment = models.TextField(help_text=u"评论内容")
    article = models.ForeignKey(Article)
    created_at = models.DateTimeField(help_text=u"创建时间", auto_now_add=True)