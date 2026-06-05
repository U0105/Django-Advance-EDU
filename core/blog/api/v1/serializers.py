from rest_framework import serializers
from blog.models import Post

class Postserializer(serializers.Serializer):

    id = serializers.IntegerField()
    author = serializers.CharField(max_length=65)
    title = serializers.CharField(max_length=65)
    status = serializers.BooleanField()
    content = serializers.CharField(max_length=255)

class PostlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id","author","status","created_date","published_date"
        ]