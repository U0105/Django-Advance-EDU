from rest_framework import serializers
from blog.models import Post, category
from accounts.models import Profile

class Postserializer(serializers.ModelSerializer):
    # status = serializers.ReadOnlyField()
    created_date = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet')
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=category.objects.all())

    class Meta:
        model = Post
        fields = ["id","author","title","content",'category',"snippet","status",'absolute_url',"created_date","published_date"]
        read_only_fields = ['author']
    
    def get_absolute_url(self,obj):

        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self,instance):
        
        rep = super().to_representation(instance)
        request = self.context.get('request')

        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet',None)
        else:
            rep.pop('content',None)

        rep['category'] = CategorySerializer(instance.category).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ["id","name"]