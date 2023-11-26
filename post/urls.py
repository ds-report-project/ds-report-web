from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create_post/', views.PostCreate.as_view(), name='post_create'),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('delete_post/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    path('category/<str:slug>/', views.category_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)