from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
import os

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/post/tag/{self.slug}/'

class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/post/category/{self.slug}/'


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    anonymous_nickname = models.CharField(
        max_length=100, blank=True, null=True, choices=ANONYMOUS_NICKNAME_CHOICES
    )
    images = models.ImageField(blank=True,null=True)
    video = models.FileField(blank=True, null=True, upload_to='post_videos/')
    attachment = models.FileField(blank=True, null=True, upload_to='post_attachments/')
    likes = models.ManyToManyField(User, related_name='post_like')
    
    def number_of_likes(self):
        return self.likes.count()
    
    resolve_actions = models.ManyToManyField(User, through='ResolveAction', related_name='resolved_posts')  # resolve에 필요
    resolve_cache = models.BooleanField(default=False) # resolved 캐시 변수 초기화

    @property
    def is_resolved(self):
        # 캐시된 결과가 있는 경우 해당 결과를 반환.
        if self.resolve_cache is not None:
            return self.resolve_cache

        # true/false 저장
        self.resolve_cache = self.resolve_actions.count() >= 1
        return self.resolve_cache

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

class Rule(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=255)

    def __str__(self):
            return self.name
          
# 해결 처리를 위해 해결 버튼 클릭 여부 저장
class ResolveAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
      
#카테고리 배열
    # FACILITIES = '시설'
    # ADMINISTRATION = '행정'
    # WELFARE = '복지'
    # EDUCATION='교육'
    # ETC='기타'
    #
    # CATEGORY_CHOICES = [
    #     (FACILITIES, '시설'),
    #     (ADMINISTRATION, '행정'),
    #     (WELFARE, '복지'),
    #     (EDUCATION, '교육'),
    #     (ETC, '기타')
    # ]

    #태그 배열
    # DORMITORY = '기숙사'
    # CLASSROOM = '강의실'
    # LIBRARY = '도서관'
    # ACCOMMODATION = '편의시설'
    # TEACHER = '교원'
    # ACADEMIC = '학사'
    # LECTURE = '강의'
    # PLANNING = '기획'
    # BUDGET = '예산'
    # IT = 'IT 서비스'
    # SCHOLARSHIP = '장학금'
    # CAFETERIA = '학식'
    # SPECIALLECTURE = '특강'
    # CURRICULUM = '커리큘럼'
    # INTERNATIONAL = '국제교류'
    # GETAJOB = '취업/창업'
    # ETC = '기타'
    #
    # TAG_CHOICES = [
    #     (DORMITORY, '기숙사'),
    #     (CLASSROOM, '강의실'),
    #     (LIBRARY, '도서관'),
    #     (ACCOMMODATION, '편의시설'),
    #     (TEACHER, '교원'),
    #     (ACADEMIC, '학사'),
    #     (LECTURE, '강의'),
    #     (PLANNING, '기획'),
    #     (BUDGET, '예산'),
    #     (IT, 'IT 서비스'),
    #     (SCHOLARSHIP, '장학금'),
    #     (CAFETERIA, '학식'),
    #     (SPECIALLECTURE, '특강'),
    #     (CURRICULUM, '커리큘럼'),
    #     (INTERNATIONAL, '국제교류'),
    #     (GETAJOB, '취업/창업'),
    #     (ETC, '기타')
    # ]
    # category = models.CharField(
    #     max_length=100, blank=True, null=True, choices=CATEGORY_CHOICES
    # )
    # tags = models.CharField(
    #     max_length=100, blank=True, null=True, choices=TAG_CHOICES
    # )
