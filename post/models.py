from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    category = models.CharField(max_length=255)
    anonymous_nickname = models.CharField(
        max_length=100, blank=True, null=True, choices=ANONYMOUS_NICKNAME_CHOICES
    )
    images=models.ImageField(blank=True,null=True)
    video = models.FileField(blank=True, null=True, upload_to='post_videos/')
    attachment = models.FileField(blank=True, null=True, upload_to='post_attachments/')

    resolve_actions = models.ManyToManyField(User, through='ResolveAction', related_name='resolved_posts')  # resolve에 필요
    resolve_cache = models.BooleanField(default=False) # resolved 캐시 변수 초기화

    @property
    def is_resolved(self):
        # 캐시된 결과가 있는 경우 해당 결과를 반환. 해결됐어요 누른 사용자가 삭제된 경우에도 해결로 분류하기 위함.
        if self.resolve_cache is not None:
            return self.resolve_cache

        # true/false 저장
        self.resolve_cache = self.resolve_actions.count() >= 1
        return self.resolve_cache
 

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    pass

# 해결 처리를 위해 해결 버튼 클릭 여부 저장
class ResolveAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')




