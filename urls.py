"""django_project_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import index, article_detail, comment_add
from django.conf.urls.static import static
import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', index, {'page': 0}),
                  url(r'^(?P<page>[0-9]+)$', index),
                  url(r'^article/(?P<id>[0-9]+)', article_detail),
                  url(r'^comment/add', comment_add),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
