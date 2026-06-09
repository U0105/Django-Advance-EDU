from rest_framework import serializers
from blog.models import Post, category

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","author","title","content","status","created_date","published_date"]
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ["id","name"]