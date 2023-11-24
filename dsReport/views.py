from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CommentForm
from .models import Comment, Post

# 댓글 작성 함수
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        comments = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = comments
            comment.user = request.user
            comment.save()
        return redirect('posts:detail', comments.pk)
    return redirect('accounts:login')

# 댓글 삭제 함수
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)