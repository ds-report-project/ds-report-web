from django.urls import reverse_lazy
from .models import Post, Category
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect


class PostCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'anonymous_nickname']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            form.instance.anonymous_nickname = "Default Nickname"  
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/post/')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate,self).form_valid(form)
        else:
            return redirect('/post/')
    
    def get_success_url(self):
        # 포스트가 성공적으로 생성된 후에 리디렉션할 URL을 지정
        return reverse_lazy('post_list') 

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        return context

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content','category']
    template_name = 'post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class PostDelete(DeleteView):
    model = Post
    success_url = '/post/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
        
