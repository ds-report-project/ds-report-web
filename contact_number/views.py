from django.shortcuts import render
from django.db import models
from post.models import Post


def contact_number(request):
    top_5_posts = Post.objects.annotate(like_count=models.Count('likes')).order_by('-like_count')[:5]
    return render(
        request,
        'contact_number/contact_number_page.html',
        {
            'top_5_posts': top_5_posts,
        }
    )
