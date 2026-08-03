from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

app = FastAPI()

posts: list[dict] = [
    {
        "id": 101,
        "author": "alex_dev",
        "title": "Understanding Python Type Hints",
        "content": "Type hints help catch bugs early and improve IDE autocompletion.",
        "tags": ["python", "coding", "backend"],
        "likes": 42,
        "is_published": True,
        "created_at": "2026-07-28T10:15:00Z",
    },
    {
        "id": 102,
        "author": "maria_arch",
        "title": "System Architecture Patterns",
        "content": "Monolith vs Microservices: choosing the right structure for scale.",
        "tags": ["architecture", "system-design", "tech"],
        "likes": 89,
        "is_published": True,
        "created_at": "2026-07-29T14:30:00Z",
    },
    {
        "id": 103,
        "author": "alex_dev",
        "title": "Drafting the Next Big Project",
        "content": "Setting up the initial repository and core dependencies.",
        "tags": ["python", "devlog"],
        "likes": 0,
        "is_published": False,
        "created_at": "2026-07-31T09:00:00Z",
    },
]

templates = Jinja2Templates(directory = "templates")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts