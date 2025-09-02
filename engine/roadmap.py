import json
from pathlib import Path

class RoadmapEngine:
    def __init__(self, syllabus_file="../data/syllabus.json"):
        self.syllabus = json.loads(Path(syllabus_file).read_text())

    def generate(self, subject):
        if subject not in self.syllabus:
            return []
        roadmap = []
        for unit, topics in self.syllabus[subject].items():
            for topic in topics:
                roadmap.append({"unit": unit, "topic": topic, "status": "pending"})
        return roadmap

