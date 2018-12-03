# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _


# from refundair.app.forms.blog import ArticleForm, EmailForm
# from refundair.app.models.blog import Article, Category


# def all_articles(request, id_category=None):
#     ARTICLES_PER_PAGE = 20
#     # most_populars = Article.objects.filter(is_published=True).order_by('-views')[:10]
#     if id_category:
#         all_articles = Article.objects.filter(is_published=True, category_id=id_category).order_by('-date')
#     else:
#         all_articles = Article.objects.filter(is_published=True).order_by('-date')
#     categories = Category.objects.all()
#     paginator = Paginator(all_articles, ARTICLES_PER_PAGE)
#     page = request.GET.get('page')
#     try:
#         articles = paginator.page(page)
#     except PageNotAnInteger:
#         articles = paginator.page(1)
#     except EmptyPage:
#         articles = paginator.page(paginator.num_pages)
#
#     template = 'blog/blog.html'
#
#     data = {
#         'articles': articles,
#         # 'most_populars': most_populars,
#         'categories': categories,
#     }
#     if all_articles.count() > ARTICLES_PER_PAGE:
#         data['is_paginated'] = True
#     return render(request, template, data)


# def get_article(request, slug):
#     article = get_object_or_404(Article, slug=slug, is_published=True)
#     most_populars = Article.objects.filter(is_published = True).order_by('-views')[:10]
#     article.views += 1
#     article.save()
#     template = 'blog/get_article.html'
#     form = EmailForm()
#     data = {
#         'article': article,
#         'most_populars': most_populars,
#         'categories': Category.objects.all(),
#         'form': form,
#     }
#     return render(request, template, data)


# def preview_article(request, slug):
#     article = get_object_or_404(Article, slug=slug)
#     most_populars = Article.objects.filter(is_published = True).order_by('-views')[:10]
#     article.views += 1
#     article.save()
#     template = 'blog/get_article.html'
#     form = EmailForm()
#     data = {
#         'article': article,
#         'most_populars': most_populars,
#         'categories': Category.objects.all(),
#         'form': form,
#     }
#     return render(request, template, data)


# @login_required(login_url='/login/')
# def new_article(request):
#     if not request.user.is_publisher:
#         raise PermissionDenied
#     form = ArticleForm(request.POST or None, request.FILES)
#     if request.method == 'POST':
#         if form.is_valid():
#             new_article = form.save(commit=False)
#             new_article.user = request.user
#             new_article.save()
#             return HttpResponseRedirect(reverse('edit_article', args=(new_article.slug,)))
#         else:
#             print('form invalid')
#             print(form.errors)
#     form = ArticleForm()
#     template = 'blog/new_article.html'
#     data = {
#         'form': form
#     }
#     return render(request, template, data)


# @login_required(login_url='/login/')
# def edit_article(request, slug):
#     if not request.user.is_publisher:
#         raise PermissionDenied
#     article = get_object_or_404(Article, slug=slug)
#     form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('edit_article', args=(article.slug,)))
#     template = 'blog/new_article.html'
#     data = {
#         'article': article,
#         'form': form
#     }
#     return render(request, template, data)


# @login_required(login_url='/login/')
# def my_articles(request):
#     if not request.user.is_publisher:
#         raise PermissionDenied
#     ARTICLES_PER_PAGE = 20
#     my_articles = Article.objects.filter(user=request.user)
#     template = 'blog/my_articles.html'
#     paginator = Paginator(my_articles, ARTICLES_PER_PAGE)
#     page = request.GET.get('page')
#     try:
#         articles = paginator.page(page)
#     except PageNotAnInteger:
#         articles = paginator.page(1)
#     except EmptyPage:
#         articles = paginator.page(paginator.num_pages)
#     data = {
#         'articles': articles
#     }
#     if my_articles.count() > ARTICLES_PER_PAGE:
#         data['is_paginated'] = True
#     return render(request, template, data)


# def email_list(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  _(u'Se ha añadido tu correo electronico correctamente') + ".")
#         else:
#             print('invalid form')
#             print(form.errors)
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))