from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import main_router
from app.core.config import settings
from app.core.log import generate_logger

logger = generate_logger()
logger.info("Starting API")

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


origins = [
    "https://deepquarry-pi.vercel.app",
    "https://deepquarry.vercel.app"
    "http://localhost",
    "http://localhost:8080",
]

regex_origin = [
    "https?//.*\.deepquarry.*vercel.app",
    "https?//.*\.localhost:?\d*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=regex_origin,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(main_router, prefix=settings.API_V1_STR)


@app.get("/")
async def main():
    return {"message": settings.PROJECT_NAME}
