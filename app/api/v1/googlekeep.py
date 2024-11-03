import os
from fastapi import APIRouter
from app.usecases.create_note_usecase import CreateNoteUseCase
from app.infrastructure.googlekeep_repository import GoogleKeepRepository

router = APIRouter()

@router.post("/keep")
async def create_keep_entry(title: str, content: str):
    # 環境変数から認証情報を取得
    username = os.getenv("GOOGLE_KEEP_USERNAME")
    app_password = os.getenv("GOOGLE_KEEP_APP_PASSWORD")

    # 環境変数が設定されていない場合はエラーを返す
    if not username or not app_password:
        return {"error": "Google Keepの認証情報が設定されていません"}

    google_keep_repo = GoogleKeepRepository(username, app_password)
    use_case = CreateNoteUseCase(google_keep_repo)
    result = use_case.execute(title, content)
    return {"result": result}

