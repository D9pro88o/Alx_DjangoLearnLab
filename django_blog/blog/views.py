from django.views.generic import ListView
from .models import Post
from taggit.models import Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'  # create this template
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        return Post.objects.filter(tags__name__iexact=tag_name)
    