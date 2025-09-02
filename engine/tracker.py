from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB("data/user_db.json")
User = Query()

def log_score(username, topic, score):
    db.insert({
        "user": username,
        "topic": topic,
        "score": score,
        "date": datetime.now().isoformat()
    })

def get_scores(username):
    return db.search(User.user == username)

