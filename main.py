from fastapi import FastAPI
from back.user_api import router as user_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user_router)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Укажите домены, которые разрешены (например, ["http://127.0.0.1:8000"])
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, DELETE, PATCH и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Добавьте монтирование статических файлов
app.mount("/front", StaticFiles(directory="front"), name="front")

# ЗАПУСК
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# http://localhost:8000/front/users.html