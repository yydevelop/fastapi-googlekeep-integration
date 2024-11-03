from fastapi import FastAPI
from app.api.v1.googlekeep import router as googlekeep_router

app = FastAPI(title="Google Keep Integration API")

# エンドポイントを登録
app.include_router(googlekeep_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the Google Keep Integration API"}
