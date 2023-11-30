from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    ANONYMOUS = '익명'
    MAJOR_SCIENCE_TECH = '과학기술대학'
    MAJOR_GLOBAL_CONVERGENCE = '글로벌융합대학'
    MAJOR_ART_DESIGN='Art & Design대학'
    MAJOR_PHARMACY='약학대학'

    ANONYMOUS_NICKNAME_CHOICES = [
        (ANONYMOUS, '익명'),
        (MAJOR_SCIENCE_TECH, '과학기술대학'),
        (MAJOR_GLOBAL_CONVERGENCE, '글로벌융합대학'),
        (MAJOR_ART_DESIGN,'Art & Design 대학'),
        (MAJOR_PHARMACY,'약학대학')
    ]

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255)
    anonymous_nickname = models.CharField(
        max_length=100, blank=True, null=True, choices=ANONYMOUS_NICKNAME_CHOICES
    )

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        content = models.CharField('*댓글을 입력하세요.', max_length=150)
        created_at = models.DateTimeField(auto_now_add=True)
        modified_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'{self.author}::{self.content}'

        def get_absolute_url(self):
            return f'{self.post.get_absolute_url()}#comment-{self.pk}'