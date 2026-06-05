from rest_framework import serializers

class Postserializer(serializers.Serializer):

    id = serializers.IntegerField()
    author = serializers.CharField(max_length=65)
    title = serializers.CharField(max_length=65)
    status = serializers.BooleanField()
    content = serializers.CharField(max_length=255)
