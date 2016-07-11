# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from article.models import Article, User, Comment

# Create your views here.


def login(request):
    errors = []
    if 'username' in request.GET:
        if request.GET['username']:
            usr = request.GET['username']
            if User.objects.filter(user=usr):
                pw = User.objects.get(user=usr).password
                if request.GET['password'] == pw:
                    return HttpResponseRedirect('/home/')
                else:
                    errors.append(u'密码错误')
                    return render_to_response('login.html', dict(error3=errors, username=usr))
            else:
                errors.append(u'用户名不存在')
                return render_to_response('login.html', dict(error2=errors, username=usr))
        else:
            errors.append(u'请输入用户名')
            return render_to_response('login.html', dict(error1=errors))
    return render_to_response('login.html')


def home(request):
    comment_list = Comment.objects.order_by('-date_time')
    return render_to_response('home.html', dict(comment_list=comment_list[:3]))


def blog(request):
    post_list = Article.objects.all()
    comment_list = Comment.objects.order_by('-date_time')
    if 'search' in request.GET:
        if request.GET['search']:
            content = request.GET['search']
            results = Article.objects.filter(title__icontains=content)
            return render_to_response('result.html', dict(results=results), context_instance=RequestContext(request))
        else:
            return HttpResponse("No results!")
    return render_to_response('blog.html', dict(post_list=post_list, comment_list=comment_list[:3]))


def detail(request, my_args):
    details = Article.objects.get(id=int(my_args))
    return render_to_response('detail.html', dict(details=details))