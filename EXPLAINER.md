# Playto Engineering Challenge – Explainer

## The Tree (Nested Comments)

For nested comments, an adjacency list approach is used, where each comment
optionally references a parent comment.

To avoid the N+1 query problem, all comments related to a post are fetched
in a single database query. Rather than relying on recursive ORM calls,
the comment hierarchy is constructed in memory using a dictionary to map
comment IDs to objects and a single pass to attach replies to their parents.

This approach keeps database access constant regardless of comment depth,
while allowing unlimited nesting with predictable and scalable performance.

---

## The Math (Leaderboard – Last 24 Hours)

Karma is calculated dynamically using a transaction log instead of being
stored directly on the User model.

Each like action creates a KarmaTransaction entry with the awarded points.
The leaderboard query filters these transactions to only include entries
from the last 24 hours, groups them by user, and aggregates the total karma
earned during that time window.

By computing the leaderboard directly from transaction history, the results
remain accurate, time-bound, and do not require maintaining separate daily
counters or scheduled reset jobs.

---

## The AI Audit

AI tools were used to accelerate early development, primarily for generating
initial scaffolding and exploring alternative architectural approaches.

One AI-generated suggestion proposed fetching nested comments using recursive
ORM queries, which would have resulted in multiple database hits and poor
scalability for deeply nested threads. This was identified during review and
replaced with a single-query fetch of all comments for a post, followed by
in-memory tree construction using an O(N) algorithm.

This adjustment ensures predictable performance, avoids N+1 query issues,
and keeps database access efficient while supporting arbitrarily deep
comment threads.
