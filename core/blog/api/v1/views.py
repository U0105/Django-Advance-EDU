from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Postserializer, PostlistSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404

@api_view()
def postlist(request):
    posts = Post.objects.filter(status=True)
    serialized = PostlistSerializer(posts,many=True)
    return Response(serialized.data)

@api_view()
def postdetail(request,id):

    post = get_object_or_404(Post,pk=id,status=True)
    serialized = Postserializer(post)
    return Response(serialized.data)