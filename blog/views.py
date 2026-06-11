from django.shortcuts import render
from .models import Post
from .models import Author, Tag

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')

    return render(request, "blog/posts.html", {
        "posts": all_posts
    })

def authors(request):
    authors = Author.objects.all()

    return render(request, "blog/authors.html", {
        "authors": authors
    })

def author_detail(request, id):
    author = Author.objects.get(id=id)

    return render(request, "blog/author_detail.html", {
        "author": author
    })

def tags(request):
    tags = Tag.objects.all()

    return render(request, "blog/tags.html", {
        "tags": tags
    })

def tag_detail(request, id):
    tag = Tag.objects.get(id=id)

    return render(request, "blog/tag_detail.html", {
        "tag": tag
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": post
    })