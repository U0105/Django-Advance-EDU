from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import Postserializer
from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postlist(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serialized = Postserializer(posts,many=True)
        return Response(serialized.data)
    elif request.method == "POST":
        serialized = Postserializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
        
@api_view(["GET","PUT","DELETE"])
def postdetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serialized = Postserializer(post)
        return Response(serialized.data)
    elif request.method == "PUT":
        serialized = Postserializer(post,data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({" detail": "Post Deleted Successfully."},status=status.HTTP_204_NO_CONTENT)