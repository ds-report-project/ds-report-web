from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create_post/', views.PostCreate.as_view(), name='post_create'),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/new_comment/', views.new_comment, name='new_comment'),
    path('delete_post/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    path('?search=<str:slug>/', views.search_page, name='search'),
    path('search/', views.post_search, name='post_search'),
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    path('post-like/<int:pk>', views.PostLike, name="post_like"),
    path('resolved/', views.PostResolvedList, name='post_resolved'),
    path('unresolved/', views.PostUnresolvedList, name='post_unresolved'),
    path('contact/', include('contact_number.urls')),
    path('accounts/', include('accounts.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
