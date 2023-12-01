from .models import Post, Category, Tag, ResolveAction
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.db import models
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'anonymous_nickname', 'images', 'video', 'attachment']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            form.instance.anonymous_nickname = form.cleaned_data.get('anonymous_nickname', "Default Nickname")
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
    
    # def get_context_data(self, **kwargs):
    #     context = super(PostList, self).get_context_data()
    #     context['categories'] = Category.objects.all()
    #     context['no_categories_post_count'] = Post.objects.filter(category=None).count()
    #     return context

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['categories'] = Category.objects.all()
        data['no_categories_post_count'] = Post.objects.filter(category=None).count()

        data['number_of_likes'] = [post.number_of_likes() for post in data['post_list']]
        return data


class PostDetail(DetailView):
    model = Post
    # def get_context_data(self, **kwargs):
    #     context = super(PostDetail, self).get_context_data()
    #     context['categories'] = Category.objects.all()
    #     context['no_categories_post_count'] = Post.objects.filter(category=None).count()
    #     return context

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['categories'] = Category.objects.all()
        data['no_categories_post_count'] = Post.objects.filter(category=None).count()

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        user = request.user

        # 사용자가 해결됐어요 버튼을 누른 적이 없는 경우에만 ResolveAction을 추가
        if 'resolve_button' in request.POST and not ResolveAction.objects.filter(user=user, post=post).exists():
            ResolveAction.objects.create(user=user, post=post)
        return HttpResponseRedirect(post.get_absolute_url())

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


#좋아요
def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
  
  
def post_search(request):
    query = request.GET.get('q')  # 검색어 가져오기

    # if len(query) == 1 :
    #     messages.error(request.request, '검색어는 2글자 이상 입력해주세요.')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환 (검색어가 없는 경우)

    return render(request, 'post/search_result.html', {'posts': posts, 'query': query})

# 해결 페이지
def PostResolvedList(request):
    post_list = Post.objects.all()
    for post in post_list:
        status = post.is_resolved()
        post.resolve_cache = status
        post.save()
    post_list = Post.objects.filter(resolve_cache=True)
    return render(
        request,
        'post/post_list.html',
        {'post_list': post_list}
    )

# 미해결 페이지
def PostUnresolvedList(request):
    post_list = Post.objects.all()
    for post in post_list:
        status = post.is_resolved()
        post.resolve_cache = status
        post.save()
    post_list = Post.objects.filter(resolve_cache=False)
    return render(
        request,
        'post/post_list.html',
        {'post_list': post_list}
    )
