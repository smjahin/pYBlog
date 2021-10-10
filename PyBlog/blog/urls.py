from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views
from blog.views import PostDetailsView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, AddCategoryView, CategoryView,AddCommentView

urlpatterns = [
    path('',PostListView.as_view(), name= 'blog-home'),
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('add_category', AddCategoryView.as_view(), name='add-category'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),

]
