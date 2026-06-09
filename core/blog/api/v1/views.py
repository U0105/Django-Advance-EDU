from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import Postserializer
from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

'''
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
'''

"""
class PostList(APIView):
    '''
    this is the class for geting list of posts and making
    new ones.
    '''

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Postserializer
    def get(self,request):
        '''
        get method for getting post lists.
        '''
        posts = Post.objects.filter(status=True)
        serialized = Postserializer(posts,many=True)
        return Response(serialized.data)
    
    def post(self,request):
        '''
        post method for posting.

        '''
        serialized = Postserializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
"""

class PostList(ListCreateAPIView):
    '''
    this is the class for geting list of posts and making
    new ones.
    '''
    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Postserializer

'''
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
'''


"""
class PostDetail(APIView):

    '''
    geting details of a post and updating it and removing it.
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Postserializer


    def get(self,request,id):

        post = get_object_or_404(Post,pk=id,status=True)
        serialized = self.serializer_class(post)
        return Response(serialized.data)

    def put(self,request,id):

        post = get_object_or_404(Post,pk=id,status=True)
        serialized = self.serializer_class(post,data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
    
    def delete(self,request,id):

        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({" detail": "Post Deleted Successfully."},status=status.HTTP_204_NO_CONTENT)
"""    

class PostDetail(RetrieveUpdateDestroyAPIView):
    '''
    geting details of a post and updating it and removing it.
    '''

    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Postserializer
    lookup_field = 'id'
