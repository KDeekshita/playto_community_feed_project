from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from feed.models import Post, Comment
from .services import like_object
from .leaderboard import get_top_users_last_24h


class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        obj_type = request.data.get('type')
        obj_id = request.data.get('id')

        if obj_type == 'post':
            obj = get_object_or_404(Post, id=obj_id)
        elif obj_type == 'comment':
            obj = get_object_or_404(Comment, id=obj_id)
        else:
            return Response({'error': 'Invalid type'}, status=400)

        like_object(user=request.user, obj=obj)
        return Response({'status': 'ok'})


class LeaderboardAPIView(APIView):
    def get(self, request):
        data = get_top_users_last_24h()
        return Response(data)
