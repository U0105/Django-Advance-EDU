from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from blog.models import Post
from django.views.generic import ListView

# Create your views here.

class IndexView(TemplateView):

    '''
        class based index view to handel a simple
        render page with GET requests.
    '''
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "hossein"
        context["posts"] = Post.objects.all()

        return context
        
class RDview(RedirectView):
    '''
        class based view to handel a redirection
        with a slug or get 404 error.
    '''
    url = "https://test.com"

    def get_redirect_url(self, *args, **kwargs):
        posts = get_object_or_404(Post, pk=kwargs["pk"])
        print(posts)
        return super().get_redirect_url(*args, **kwargs)

class CBListview(ListView):
    # model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    ordering = '-id'
    # def get_queryset(self):
        # posts = Post.objects.filter(status=True)
        # return posts