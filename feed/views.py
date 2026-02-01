from rest_framework.generics import RetrieveAPIView
from .models import Post
from .serializers import PostDetailSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.select_related('author')
    serializer_class = PostDetailSerializer
