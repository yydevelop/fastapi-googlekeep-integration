from datetime import datetime

class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
