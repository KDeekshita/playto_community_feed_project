# Playto Engineering Challenge – Explainer

## The Tree (Nested Comments)
For nested comments, I used an adjacency list approach where each comment,
optionally references a parent comment.

To avoid the N+1 query problem, all comments related to a post are fetched,
in a single database query. Instead of relying on recursive ORM calls,
the comment hierarchy is built in memory using a dictionary to map,
comment IDs to objects and a single pass to attach replies to their parents.

This approach keeps database access constant regardless of how deep the,comment threads are, while allowing unlimited nesting with predictable performance.

## The Math (Leaderboard – Last 24 Hours)
Karma is calculated dynamically using a transaction log instead of being stored on the User model.

Each like action creates a KarmaTransaction entry with the awarded points.
The leaderboard query filters these transactions to only include entries,
from the last 24 hours, groups them by user, and aggregates the total karma earned during that time window.

By computing the leaderboard directly from transaction history, the
results are always accurate, time-bound, and do not require maintaining separate daily counters or scheduled reset jobs.

## The AI Audit
AI tools were used to accelerate development, especially for generating
initial scaffolding and exploring alternative designs.

One issue encountered was an AI-generated suggestion to fetch nested
comments using recursive ORM queries, which would have resulted in
multiple database hits and poor scalability. This was identified and
replaced with a single-query approach and in-memory tree construction,
ensuring efficient database usage and predictable performance.
