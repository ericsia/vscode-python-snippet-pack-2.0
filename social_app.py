from fastapi import FastAPI, HTTPException, UploadFile, File, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import databases
import sqlalchemy
from datetime import datetime
import json
import os

# تنظیمات پایگاه داده
DATABASE_URL = "sqlite:///./social_app.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# مدل‌های پایگاه داده
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(100)),
    sqlalchemy.Column("email", sqlalchemy.String(100)),
    sqlalchemy.Column("full_name", sqlalchemy.String(100)),
    sqlalchemy.Column("profile_pic", sqlalchemy.String(200)),
    sqlalchemy.Column("language", sqlalchemy.String(10), default="fa"),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
)

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("content", sqlalchemy.String(1000)),
    sqlalchemy.Column("image_url", sqlalchemy.String(200)),
    sqlalchemy.Column("likes", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
)

messages = sqlalchemy.Table(
    "messages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("sender_id", sqlalchemy.Integer),
    sqlalchemy.Column("receiver_id", sqlalchemy.Integer),
    sqlalchemy.Column("content", sqlalchemy.String(500)),
    sqlalchemy.Column("message_type", sqlalchemy.String(20)),  # text, image, voice
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
)

stories = sqlalchemy.Table(
    "stories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("image_url", sqlalchemy.String(200)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
)

# مدل‌های Pydantic
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    full_name: str

class UserLogin(BaseModel):
    username: str
    password: str

class PostCreate(BaseModel):
    user_id: int
    content: str
    image_url: Optional[str] = None

class MessageCreate(BaseModel):
    sender_id: int
    receiver_id: int
    content: str
    message_type: str = "text"

app = FastAPI(title="Social App", description="یک شبکه اجتماعی کامل")

# CORS برای ارتباط با فرانت‌اند
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# دیکشنری برای ترجمه‌ها
translations = {
    "fa": {
        "welcome": "خوش آمدید",
        "login_success": "ورود موفقیت‌آمیز",
        "register_success": "ثبت نام موفقیت‌آمیز"
    },
    "en": {
        "welcome": "Welcome",
        "login_success": "Login successful",
        "register_success": "Registration successful"
    },
    "ps": {
        "welcome": "ښه راغلست",
        "login_success": "بریالۍ ننوتل",
        "register_success": "بریالۍ نوم ثبتول"
    }
}

# WebSocket برای چت زنده
connected_clients = []

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # ارسال پیام به همه کاربران
            for client in connected_clients:
                await client.send_text(f"User {user_id}: {data}")
    except:
        connected_clients.remove(websocket)

@app.on_event("startup")
async def startup():
    await database.connect()
    # ایجاد جداول
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# routes
@app.post("/register/")
async def register_user(user: UserCreate):
    # بررسی وجود کاربر
    query = users.select().where(users.c.username == user.username)
    existing_user = await database.fetch_one(query)
    
    if existing_user:
        raise HTTPException(status_code=400, detail="نام کاربری already exists")
    
    # ایجاد کاربر جدید
    query = users.insert().values(
        username=user.username,
        password=user.password,  # در واقعیت باید هش شود
        email=user.email,
        full_name=user.full_name
    )
    user_id = await database.execute(query)
    
    return {
        "user_id": user_id, 
        "message": "کاربر با موفقیت ثبت نام کرد",
        "translation": translations["fa"]["register_success"]
    }

@app.post("/login/")
async def login_user(user: UserLogin):
    query = users.select().where(users.c.username == user.username)
    db_user = await database.fetch_one(query)
    
    if db_user and db_user.password == user.password:
        return {
            "message": "ورود موفق",
            "user_id": db_user.id,
            "username": db_user.username,
            "full_name": db_user.full_name,
            "translation": translations["fa"]["login_success"]
        }
    else:
        raise HTTPException(status_code=400, detail="نام کاربری یا رمز عبور اشتباه")

@app.post("/create_post/")
async def create_post(post: PostCreate):
    query = posts.insert().values(
        user_id=post.user_id,
        content=post.content,
        image_url=post.image_url
    )
    post_id = await database.execute(query)
    return {"post_id": post_id, "message": "پست ایجاد شد"}

@app.get("/posts/")
async def get_posts():
    query = posts.select().order_by(posts.c.created_at.desc())
    return await database.fetch_all(query)

@app.post("/like_post/{post_id}")
async def like_post(post_id: int):
    query = posts.select().where(posts.c.id == post_id)
    post = await database.fetch_one(query)
    
    if post:
        new_likes = post.likes + 1
        query = posts.update().where(posts.c.id == post_id).values(likes=new_likes)
        await database.execute(query)
        return {"message": "پست لایک شد", "new_likes": new_likes}
    
    raise HTTPException(status_code=404, detail="پست پیدا نشد")

@app.post("/send_message/")
async def send_message(message: MessageCreate):
    query = messages.insert().values(
        sender_id=message.sender_id,
        receiver_id=message.receiver_id,
        content=message.content,
        message_type=message.message_type
    )
    message_id = await database.execute(query)
    return {"message_id": message_id, "status": "پیام ارسال شد"}

@app.get("/messages/{user_id}/{other_user_id}")
async def get_messages(user_id: int, other_user_id: int):
    query = messages.select().where(
        ((messages.c.sender_id == user_id) & (messages.c.receiver_id == other_user_id)) |
        ((messages.c.sender_id == other_user_id) & (messages.c.receiver_id == user_id))
    ).order_by(messages.c.created_at)
    return await database.fetch_all(query)

@app.get("/users/")
async def get_users():
    query = users.select()
    return await database.fetch_all(query)

# سیستم کتاب و اشعار
@app.get("/poetry/{poet}")
async def get_poetry(poet: str):
    poetry_data = {
        "saadi": [
            "بنى آدم اعضای یک پیکرند",
            "که در آفرینش ز یک گوهرند"
        ],
        "molana": [
            "بیا بیا که تویی جان جان جان",
            "بیا که قند تو شد جان جان جان"
        ],
        "khayam": [
            "این کوزه چو من عاشق زاری بوده است",
            "در بند سر زلف نگاری بوده است"
        ]
    }
    return poetry_data.get(poet, ["شاعر پیدا نشد"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
