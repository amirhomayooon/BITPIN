
from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Post

# Get all products in random order


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('?')
    serializer_class = PostSerializer
