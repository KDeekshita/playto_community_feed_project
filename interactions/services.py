from django.db import transaction, IntegrityError
from django.contrib.contenttypes.models import ContentType

from .models import Vote, KarmaTransaction
from feed.models import Post, Comment


def like_object(*, user, obj):
    """
    Safely like a Post or Comment.
    Prevents double likes and awards karma exactly once.
    """

    content_type = ContentType.objects.get_for_model(obj)

    try:
        with transaction.atomic():
            vote = Vote.objects.create(
                user=user,
                content_type=content_type,
                object_id=obj.id,
            )

            if isinstance(obj, Post):
                karma = 5
                recipient = obj.author
            elif isinstance(obj, Comment):
                karma = 1
                recipient = obj.author
            else:
                return

            KarmaTransaction.objects.create(
                user=recipient,
                amount=karma,
                vote=vote
            )

    except IntegrityError:
        # User already liked this object
        pass
