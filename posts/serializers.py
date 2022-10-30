from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    rating = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ['id', 'body', 'rating']
