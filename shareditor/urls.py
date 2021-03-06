"""shareditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='homepage'),
    url(r'^bloglistbytag/', views.blog_list_by_tag, name='blog_list_by_tag'),
    url(r'^blogshow', views.blog_show, name='blog_show'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^uploader/body_upload', views.body_upload, name='body_upload'),
    url(r'^chatbot/$', views.chatbotv6, name='chatbot'),
    url(r'^chatbotv6/$', views.chatbotv6, name='chatbotv6'),
    url(r'^chatbot/query$', views.chatbot_query, name='chatbot_query'),
    url(r'^chatbot/bad_question$', views.bad_question, name='bad_question'),
    url(r'^chatbot/like_answer$', views.like_answer, name='like_answer'),
    url(r'^chatbot/udf_answer$', views.udf_answer, name='udf_answer'),
    url(r'^chatbot_querytest$', views.chatbot_querytest, name='chatbot_querytest'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='static/robots.txt')),
    url(r'^bdunion.txt$', TemplateView.as_view(template_name='static/bdunion.txt')),
    url(r'^report/pv.gif$', views.report_pv, name='report_pv'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
