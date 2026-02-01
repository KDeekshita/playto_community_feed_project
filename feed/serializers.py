from rest_framework import serializers
from .models import Post, Comment


class RecursiveCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'replies']

    def get_replies(self, obj):
        # Safe: replies is an in-memory list, not a queryset
        return RecursiveCommentSerializer(obj.replies, many=True).data


class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'comments']

    def get_comments(self, obj):
        from .services import build_comment_tree
        roots = build_comment_tree(obj.id)
        return RecursiveCommentSerializer(roots, many=True).data
