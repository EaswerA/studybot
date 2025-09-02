import streamlit as st
from ..engine.roadmap import RoadmapEngine
from ..engine.spaced_repetition import SpacedRepetitionEngine
from ..engine.tracker import ProgressTracker
from ..models.question_generator import QuestionGenerator

st.set_page_config(page_title="StudyBot", page_icon="📘", layout="centered")

roadmap_engine = RoadmapEngine()
tracker = ProgressTracker()
spaced = SpacedRepetition()
qgen = QuestionGenerator()

st.title("📘 StudyBot - Your Exam Assistant")

username = st.text_input("Enter your name:")

subject = st.selectbox("Choose a subject:", ["Mathematics", "Physics"])

if st.button("Generate Roadmap"):
    roadmap = roadmap_engine.generate(subject)
    for r in roadmap:
        st.write(f"- {r['unit']} → {r['topic']} [{r['status']}]")

topic = st.text_input("Enter topic to practice:")
if st.button("Get Quiz Question"):
    if topic:
        question = qgen.generate_question(f"Explain the topic: {topic}")
        st.write("**Generated Question:**", question)

if st.button("Mark as Completed"):
    if topic and username:
        tracker.update(username, topic, "completed")
        st.success(f"{topic} marked as completed!")

if st.button("Set Review Schedule"):
    if topic:
        schedule = spaced.review_time(topic, level=2)
        st.json(schedule)

