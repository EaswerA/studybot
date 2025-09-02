import datetime

class SpacedRepetition:
    def __init__(self):
        self.schedule = {}

    def review_time(self, topic, level=1):
        """Set next review time based on success level"""
        days = {1: 1, 2: 3, 3: 7, 4: 14}
        next_time = datetime.datetime.now() + datetime.timedelta(days=days.get(level, 1))
        self.schedule[topic] = str(next_time)
        return self.schedule

