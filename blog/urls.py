from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>/", views.post_detail, name="posts-detail-page"),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:id>/", views.author_detail, name="author-detail"),
    path("tags/", views.tags, name="tags"),
    path("tags/<int:id>/", views.tag_detail, name="tag-detail"),
]