from django.urls import path
from .views import PostSearchAPIView

urlpatterns = [
    # 다른 URL 패턴들...
    path('api/posts/search/', PostSearchAPIView.as_view(), name='post-search'),
    # 다른 URL 패턴들...
]