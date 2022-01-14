from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostsList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
