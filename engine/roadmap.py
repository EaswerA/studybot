import math
import json

def load_syllabus(subject):
    with open("data/syllabus.json") as f:
        data = json.load(f)
    return data.get(subject.lower(), [])

def create_study_plan(subject, days):
    topics = load_syllabus(subject)
    if not topics:
        return []

    per_day = math.ceil(len(topics) / days)
    plan = [topics[i:i + per_day] for i in range(0, len(topics), per_day)]
    return plan

plan = create_study_plan("neet_biology", 5)
for i, day in enumerate(plan):
    print(f"Day {i+1}: {day}")

