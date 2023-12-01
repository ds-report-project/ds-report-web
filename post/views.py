from django.db import models
from .models import Post, Category, Tag, Comment, Rule
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.http import JsonResponse
from django.http import HttpResponseRedirect



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

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
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

#카테고리 별 상세페이지
def category_page(request, slug):
    if slug == 'no_category':
        category = '기타'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'post/post_list.html',
    {
        'post_list' : post_list,
        'categories' : Category.objects.all(),
        'no_categories_post_count' : Post.objects.filter(category=None).count(),
        'category' : category,
    }
    )

        
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            new_comment = request.POST['new_comment']
            post_id = request.path.split('/')[3]

            if new_comment:
                comment = Comment(post_id=post_id, author=request.user, content=new_comment)

                comment.save()
                return redirect(post.get_absolute_url())  # post or comment
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/update_comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_comment(request, pk):
    comment_id = request.path.split('/')[3]

    comment = Comment.objects.filter(id=comment_id)[0]
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


# def delete_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post = comment.post

#     if request.user.is_authenticated and request.user == comment.author:
#         comment.delete()
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Permission denied'}, status=403)
#태그
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'post/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count()
        }
    )

# 키워드 검색
def search_page(request, slug):
    print(f'search_page: {slug}') #검색 키워드

    searched_queryset = Rule.objects.filter(name=slug).all()
    # searched_list=list(searched_queryset)
    # print(f"current url: {request.path}")
    # print(f"searched url: {searched_list}")
    # print(f"name: {searched_queryset.values()}")
    # print(f"name: {searched_queryset.values()[0]['name']}")
    # print(f"name: {searched_queryset.values()[0]['content']}")

    # Your logic to get context_data
    if searched_queryset.values():
        context_data = {searched_queryset.values()[0]['name'] : searched_queryset.values()[0]['content']}
    else:
         context_data = {}

    # Save the context_data in the session
    request.session['search_context'] = context_data

    return redirect(request.path)


# class RuleList(ListView):
#     model = Post
#     ordering = '-pk'

#     def get_context_data(self, **kwargs):
#         searched = self.request.GET.get('searched')
#         print(f'searched: {searched}')
#         context = {'message': searched}
#         return context
    