# -*- coding:utf-8 -*-

from django.db import models
from PIL import Image


# Create your models here.

class Article(models.Model):
    title = models.TextField(help_text=u"标题")
    image = models.ImageField(help_text=u"图片")
    content = models.TextField(help_text=u"内容")
    created_at = models.DateTimeField(help_text=u"创建时间", auto_now_add=True)

    def save(self):
        super(Article, self).save()

        image = Image.open(self.image)
        ori_width, ori_height = image.size
        if ori_width > 1024:
            ratio = float(ori_width) / float(ori_height)
            size = (1024, int(float(1024)/float(ratio)))
            image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)


class Comment(models.Model):
    name = models.TextField(help_text=u"评论标题")
    comment = models.TextField(help_text=u"评论内容")
    article = models.ForeignKey(Article)
    created_at = models.DateTimeField(help_text=u"创建时间", auto_now_add=True)
