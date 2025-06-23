from fastapi import FastAPI
from app.features.ingest.api import ingest_controller
from app.config.settings import settings
from app.features.search.api import search_controller
from app.features.answer.api.answer_controller import router as answer_router
from app.features.ingest.api.ingest_file_controller import router as ingest_file_router
from app.features.ingest.api.ingest_code_file_controller import router as ingest_code_file_router

app = FastAPI(title="CodexMind Embedding API")

# Registro de routers
app.include_router(ingest_controller.router, prefix="/api")
app.include_router(ingest_file_router, prefix="/api")
app.include_router(ingest_code_file_router, prefix="/api")
app.include_router(search_controller.router, prefix="/api")
app.include_router(answer_router, prefix="/api")

print("🧠 Embedding Provider activo:", settings.EMBEDDING_PROVIDER)
