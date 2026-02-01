from .models import Comment


def build_comment_tree(post_id):
    """
    Build a nested comment tree for a post in O(N) time
    using a single database query.
    """

    # 1. Fetch all comments for the post in ONE query
    comments = (
        Comment.objects
        .filter(post_id=post_id)
        .select_related('author')
        .order_by('created_at')
    )

    # 2. Build lookup map
    comment_map = {comment.id: comment for comment in comments}

    roots = []

    # 3. Initialize replies list on each comment
    for comment in comments:
        comment.replies = []

    # 4. Link children to parents
    for comment in comments:
        if comment.parent_id:
            parent = comment_map.get(comment.parent_id)
            if parent:
                parent.replies.append(comment)
            else:
                # orphan comment, treat as root
                roots.append(comment)
        else:
            roots.append(comment)

    return roots
