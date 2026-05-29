from fastapi import FastAPI
from pydantic import BaseModel
import requests
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

WEBHOOK_URL = "https://discord.com/api/webhooks/1509728987251867799/H1W114mmUQXolEmv-5Cl3oIc9O8hMqBlLdeB4Px4m28qQ7qChyYQOFr8wXQG3Dlq5Jg9"

def init_db():
    conn = sqlite3.connect('comments.db')
    conn.execute('CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, post_id TEXT, author TEXT, text TEXT)')
    conn.commit()
    conn.close()

init_db()

class Comment(BaseModel):
    postId: str
    author: str
    text: str

@app.post("/api/comments")
async def add_comment(c: Comment):
    # Сохранение в БД
    conn = sqlite3.connect('comments.db')
    conn.execute("INSERT INTO comments (post_id, author, text) VALUES (?, ?, ?)", (c.postId, c.author, c.text))
    conn.commit()
    conn.close()
    
    # Отправка в Discord
    try:
        requests.post(WEBHOOK_URL, json={
            "content": f"📩 **Новый комментарий в посте {c.postId}**\n**Автор:** {c.author}\n**Текст:** {c.text}"
        })
    except Exception as e:
        print(f"Ошибка отправки в Discord: {e}")
        
    return {"status": "ok"}

@app.get("/api/comments")
async def get_comments(postId: str):
    conn = sqlite3.connect('comments.db')
    cursor = conn.execute("SELECT author, text FROM comments WHERE post_id = ?", (postId,))
    data = [{"author": r[0], "text": r[1]} for r in cursor.fetchall()]
    conn.close()
    return data