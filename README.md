# Community Feed – Playto Engineering Challenge

This repository contains my solution for the **Playto Community Feed engineering challenge**.
The implementation focuses on backend correctness, performance, and data integrity, as
highlighted in the problem statement.

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (used for local development; schema and queries are fully compatible with PostgreSQL as suggested in the challenge)
- **Language:** Python

---

## Features Implemented

### Community Feed
- Users can create text-based posts.
- Each post has an author and supports likes.

### Threaded Comments
- Users can comment on posts and reply to other comments using nested threads.
- Comments are modeled using an adjacency list with a self-referencing parent field.
- All comments for a post are fetched in a single database query.
- The nested comment tree is constructed in memory to avoid 
N+1 query issues.

### Gamification (Karma System)
- Liking a post awards **+5 karma** to the post author.
- Liking a comment awards **+1 karma** to the comment author.
- Karma is recorded as immutable transaction entries rather than stored counters.

### Concurrency Safety
- A user can like a post or comment only once.
- Database-level unique constraints prevent duplicate likes.
- Like creation and karma assignment are executed inside atomic transactions.

### Leaderboard (Last 24 Hours)
- Displays the top users based on karma earned in the last 24 hours only.
- Leaderboard values are calculated dynamically from the karma transaction history.

---

## API Endpoints

### Get Post with Nested Comments
```
GET /api/posts/<id>/
```

Returns a single post along with all nested comments in one response.

---

### Like a Post or Comment
```
POST /api/like/
```

Request body example:
```json
{
  "type": "post",
  "id": 1
}
```

or

```json
{
  "type": "comment",
  "id": 5
}
```

---

### Leaderboard (Last 24 Hours)
```
GET /api/leaderboard/
```

Returns the top users ranked by karma earned in the last 24 hours only.

---

## Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Server runs at:
```
http://127.0.0.1:8000/
```

---

## Admin Interface

Django admin is available at:
```
http://127.0.0.1:8000/admin/
```

It can be used to create users, posts, comments, and inspect votes and karma transactions.

---

## Additional Documentation

Design decisions and architecture explanations are documented in `EXPLAINER.md`.
