# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Post
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return  Post.objects.order_by('-post_pub_date')[:3]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

#def index(request):
#    latest_posts = Post.objects.order_by('-post_pub_date')[:3]
#    context = {'latest_posts': latest_posts}
#    return render(request, 'blog/index.html', context)

#def detail(request, post_id):
#    post = get_object_or_404(Post, pk=post_id)
#    return render(request,'blog/detail.html', {'post': post})
