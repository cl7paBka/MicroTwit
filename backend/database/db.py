from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from backend.utils.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Подключение к бд
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Асинхронный PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика асинхронных сессий
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Базовый класс моделей в backend.models
class Base(DeclarativeBase):
    pass


# Инициализация БД и создание таблиц, происходящее при запуске
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Асинхронно генерируем сессии
async def get_async_session():
    async with async_session_maker() as session:
        yield session
