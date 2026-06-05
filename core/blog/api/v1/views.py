from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Postserializer
from blog.models import Post

@api_view()
def postlist(request):
    return Response("ok")

@api_view()
def postdetail(request,id):

    post = Post.objects.get(pk=id)
    serialized = Postserializer(post)
    return Response(serialized.data)