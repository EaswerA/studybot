import json
from pathlib import Path

class ProgressTracker:
    def __init__(self, user_file="../data/user_db.json"):
        self.user_file = Path(user_file)
        if not self.user_file.exists():
            self.user_file.write_text(json.dumps({"users": {}}))
        self.data = json.loads(self.user_file.read_text())

    def update(self, username, topic, status):
        user = self.data["users"].setdefault(username, {})
        user[topic] = status
        self.user_file.write_text(json.dumps(self.data, indent=2))

