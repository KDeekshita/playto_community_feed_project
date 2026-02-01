from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum

from .models import KarmaTransaction


def get_top_users_last_24h(limit=5):
    since = timezone.now() - timedelta(hours=24)

    return (
        KarmaTransaction.objects
        .filter(created_at__gte=since)
        .values('user__id', 'user__username')
        .annotate(score=Sum('amount'))
        .order_by('-score')[:limit]
    )
