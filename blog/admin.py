# -*- coding:utf-8 -*-
from django.contrib import admin
from django.forms.models import ModelForm
from PIL import Image
from blog.models import Article, Comment
from cStringIO import StringIO
from django.core.files.base import ContentFile


# Register your models here.

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()

        # for k in dir(cleaned_data['image']):
        #     print str(getattr(cleaned_data['image'], k, '')) + '\n'
        # f = StringIO()
        # try:
        #     pil_image_obj = Image.open(cleaned_data['image'])
        #     pil_image_obj.save(f, format='jpeg')
        #     self.image.save()
        # finally:
        #     f.close()

        return cleaned_data


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    form = ArticleForm


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'article']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
