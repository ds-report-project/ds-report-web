from django.shortcuts import redirect
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'anonymous_nickname', 'images', 'video', 'attachment']

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

    def get_success_url(self):
        return reverse_lazy('post_list')


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'anonymous_nickname', 'images', 'video', 'attachment']
    template_name = 'post/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context


class PostDelete(DeleteView):
    model = Post
    success_url = '/post/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

        
