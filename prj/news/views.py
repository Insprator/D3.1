from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'posts.html'
    context_object_name = 'newsposts'

    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'newspost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')