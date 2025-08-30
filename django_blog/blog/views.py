from django.shortcuts import render
from django.db.models import Q
from .models import Post
from taggit.models import Tag

def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct() if query else Post.objects.none()

    return render(request, 'blog/search_results.html', {'posts': results, 'query': query})

def tagged_posts(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, 'blog/tagged_posts.html', {'posts': posts, 'tag': tag})
