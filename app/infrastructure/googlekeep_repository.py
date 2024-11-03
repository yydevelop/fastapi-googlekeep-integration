import gkeepapi
from app.domain.models.note import Note

class GoogleKeepRepository:
    def __init__(self, username: str, app_password: str):
        self.keep = gkeepapi.Keep()
        self.keep.login(username, app_password)

    def save(self, note: Note):
        gnote = self.keep.createNote(note.title, note.content)
        self.keep.sync()
        return {"status": "success", "title": gnote.title, "content": gnote.text}
