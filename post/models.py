from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    anonymous_nickname = models.CharField(
        max_length=100, blank=True, null=True, choices=ANONYMOUS_NICKNAME_CHOICES
    )

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])