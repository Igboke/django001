from django.urls import path
from . import views #or just import views?
from .views import PostListView,PostCreateView,PostUpdateView,PostDeleteView, UserPostListView

app_name = 'blog'

urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('user/<str:username>/',UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail_view,name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:post_id>/share/',views.post_share,name='post-share')
]