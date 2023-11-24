from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import pandas as pd

# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/앱 이름/category/{self.slug}'


# 태그
class Tag(models.Model): 
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/앱 이름/tag/{self.slug}'


# 게시물
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True) # 게시물 공감
    is_resolved = models.BooleanField(default=False)  # 해결인 경우 True

    # 검색 ####################
    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )


	# 최신순 게시글 정렬 기능 추가 ####################
    @classmethod
    def latest_posts(cls):
        return cls.objects.order_by('-created_at')

    # 공감순 게시글 정렬 기능 추가 ####################
    @classmethod
    def popular_posts(cls):
        return cls.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')

    # 댓글순 게시글 정렬 기능 추가 ####################
    @classmethod
    def commented_posts(cls):
        return cls.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')

    # 공감 많은 순 상위 5개 게시물 뽑기 ####################
    @classmethod
    def top_five_popular_posts(cls):
        top_five = cls.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]
        return top_five


# 공감 기능(게시물, 댓글)
class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # 추천한 글 모아볼 때 최신순으로 정렬하기 위해 시간 기록
    created_at = models.DateTimeField(auto_now_add=True)

    # 다대일 관계:한 유저가 여러 개의 추천.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()  # id는 항상 양수

    # 이름을 content_type, object_id로 지으면 위의 파라미터 없어도 됨.
    liked_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"({self.user}, {self.liked_object})"


# 이미지 첨부
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='post_images/')


# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


# 공감 기능(게시물, 댓글)
class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # 추천한 글 모아볼 때 최신순으로 정렬하기 위해 시간 기록
    created_at = models.DateTimeField(auto_now_add=True)

    # 다대일 관계:한 유저가 여러 개의 추천.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()  # id는 항상 양수

    # 이름을 content_type, object_id로 지으면 위의 파라미터 없어도 됨.
    liked_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"({self.user}, {self.liked_object})"


# 규정 검색 기능
class ExcelData(models.Model):
    file = models.FileField(upload_to='uploads/')

    @staticmethod
    def search_data(search_term):
        excel_data = pd.read_excel(ExcelData.file.path)
        result_data = excel_data[excel_data['Column_Name'].str.contains(search_term, case=False)]
        result_list = result_data.to_dict(orient='records')

        return result_list