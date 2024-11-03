from app.domain.models.note import Note
from app.infrastructure.googlekeep_repository import GoogleKeepRepository

class CreateNoteUseCase:
    def __init__(self, google_keep_repo: GoogleKeepRepository):
        self.google_keep_repo = google_keep_repo

    def execute(self, title: str, content: str):
        note = Note(title, content)
        return self.google_keep_repo.save(note)
