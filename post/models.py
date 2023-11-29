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


    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # category = models.CharField(
    #     max_length=100, blank=True, null=True, choices=CATEGORY_CHOICES
    # )

    tags = models.ManyToManyField(Tag, blank=True)
    # tags = models.CharField(
    #     max_length=100, blank=True, null=True, choices=TAG_CHOICES
    # )
    anonymous_nickname = models.CharField(
        max_length=100, blank=True, null=True, choices=ANONYMOUS_NICKNAME_CHOICES
    )
    images=models.ImageField(blank=True,null=True)
    video = models.FileField(blank=True, null=True, upload_to='post_videos/')
    attachment = models.FileField(blank=True, null=True, upload_to='post_attachments/')
 

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    pass






